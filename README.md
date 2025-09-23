*Assuming you have ROS 2 Humble and Gazebo Harmonic running on Ubuntu 22.04*
*I apologize that the folder is named ros2 and not something like "pendulum_ros" I will fix soon*

Download ros2 and gazebo folders

move ros2 folder into ros_ws

cd ~/ros_ws/ros2

colcon build --packages-select crazyflie_pendulum_sim

colcon build --packages-select pendulum_pkg

source ~/ros2_ws/install/setup.bash

ros2 launch crazyflie_pendulum_sim sim.launch.py

ros2 run pendulum_pkg control_node
