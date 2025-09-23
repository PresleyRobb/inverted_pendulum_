*Assuming you have ROS 2 Humble and Gazebo Harmonic running on Ubuntu 22.04*

Download pendulum_ros and gazebo folders

move pendulum_ros folder into ros_ws

cd ~/ros_ws/pendulum_ros

colcon build --packages-select crazyflie_pendulum_sim

colcon build --packages-select pendulum_pkg

source ~/ros2_ws/install/setup.bash

ros2 launch crazyflie_pendulum_sim sim.launch.py

ros2 run pendulum_pkg control_node
