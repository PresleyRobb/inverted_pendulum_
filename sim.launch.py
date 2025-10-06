from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch_ros.actions import Node
import os

WORLD = os.path.expanduser('~/ros2_humble/src/inverted_pendulum/models/worlds/working_pendulum.world')

def generate_launch_description():
    return LaunchDescription([
        ExecuteProcess(
            cmd=['gz', 'sim', '--verbose', '-r', WORLD],
            output='screen'),
            
       Node(
            package='ros_gz_bridge',
            executable='parameter_bridge',
            arguments=[
                # ROS → Gazebo
                '/model/pendulum_cart/cmd_vel@geometry_msgs/msg/Twist]gz.msgs.Twist',
                '/crazyflie/gazebo/command/twist@geometry_msgs/msg/Twist@gz.msgs.Twist',
                # Gazebo → ROS
                '/model/crazyflie/odometry@nav_msgs/msg/Odometry@gz.msgs.Odometry',
                '/model/pendulum_cart/odometry@nav_msgs/msg/Odometry@gz.msgs.Odometry',
            ],
            output='screen'),
    ])
