#!/bin/bash

echo "Attempting to kill ROS processes..."

# Get the PIDs of the running ROS nodes based on your ps output
PIDS=$(ps aux | grep -iE 'joy_node|joy_teleop|ackermann_to_vesc_node|vesc_to_odom_node|vesc_driver_node|ackermann_mux' | grep -v grep | awk '{print $2}')

if [ -z "$PIDS" ]; then
  echo "No specific ROS node processes found."
else
  echo "Killing PIDs: $PIDS"
  kill -9 $PIDS
  echo "Kill command sent."
fi

# Also try the general pkill for any other ROS processes
echo "Attempting general ROS pkill..."
pkill -9 -f ros

echo "Cleaning up ROS 2 shared memory..."
sudo rm -rf /dev/shm/fastrtps*

echo "Done. Checking remaining ROS processes:"
ps aux | grep ros | grep -v grep

echo "Script finished."
