*Assuming you have ROS 2 Humble and Gazebo Harmonic running on Ubuntu 22.04*

Download ros and gazebo folders

cd ~/ros

colcon build --packages-select crazyflie_pendulum_sim

colcon build --packages-select pendulum_pkg

ros2 launch crazyflie_pendulum_sim sim.launch.py

ros2 run pendulum_pkg control_node
