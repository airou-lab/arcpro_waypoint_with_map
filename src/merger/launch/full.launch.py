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
            {'wheelbase': 0.33},       # example
            {'use_stamps': False}
        ]
    )


    return LaunchDescription([
        launch.actions.DeclareLaunchArgument(name='use_sim_time', default_value='false'),
        IncludeLaunchDescription(
            PathJoinSubstitution([
                FindPackageShare('waypoint_with_map'),
                'launch',
                'waypointer.launch.py'
            ])
        ),
        twist_to_ackermann,

    ])