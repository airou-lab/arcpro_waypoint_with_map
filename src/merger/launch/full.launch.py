import os
import launch
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    twist_to_ackermann = Node(
        package='twist_to_ackermann',
        executable='twist_to_ackermann',
        name='twist_to_ackermann',
        parameters=[
            {'wheelbase': 0.33},  # example
            {'use_stamps': False}
        ]
    )
    rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
#        arguments=['-d', os.path.join(
#            FindPackageShare('waypoint_with_map').find('waypoint_with_map'),
#            'rviz',
#            'waypointer.rviz'  # your rviz config file
#        )],
        output='screen'
    )


    return LaunchDescription([
        launch.actions.DeclareLaunchArgument(name='use_sim_time', default_value='false'),
        # nav2\
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                PathJoinSubstitution([
                    FindPackageShare('nav2_bringup'),
                    'launch',
                    'navigation_launch.py'
                ])
            ),
            launch_arguments={
                'params_file': PathJoinSubstitution([
                   FindPackageShare('merger'),
                   'config',
                   'nav2.yaml'
                ]),
                'use_sim_time': 'false',
                'use_docking': 'False' ,
            }.items()
        ),
        #vsec
        # IncludeLaunchDescription(
        #     PathJoinSubstitution([
        #         FindPackageShare('launches'),
        #         'launch',
        #         'vesc.launch.py'
        #     ])
        # ),
        IncludeLaunchDescription(
            PathJoinSubstitution([
                FindPackageShare('f1tenth_stack'),
                'launch',
                'no_lidar_bringup_launch.py'
            ])
        ),
        #ldiar
#ros2 launch launch ydlidar_launch.py
        IncludeLaunchDescription(
            PathJoinSubstitution([
                FindPackageShare('ydlidar_ros2_driver'),
                'launch',
                'ydlidar_launch.py'
            ])
        ),
        twist_to_ackermann,
        rviz_node,
    ])
