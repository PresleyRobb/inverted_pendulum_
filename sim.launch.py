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
                '/model/pendulum_cart/cmd_vel@geometry_msgs/msg/Twist@gz.msgs.Twist',
                '/world/pendulum_world/model/pendulum_cart/joint/br_wheel/cmd_vel@std_msgs/msg/Float64]gz.msgs.Double',
                '/world/pendulum_world/model/pendulum_cart/joint/fr_wheel/cmd_vel@std_msgs/msg/Float64]gz.msgs.Double',
                '/world/pendulum_world/model/pendulum_cart/joint/bl_wheel/cmd_vel@std_msgs/msg/Float64]gz.msgs.Double',
                '/world/pendulum_world/model/pendulum_cart/joint/fl_wheel/cmd_vel@std_msgs/msg/Float64]gz.msgs.Double',
                # Gazebo → ROS
                '/model/pendulum_cart/odometry@nav_msgs/msg/Odometry@gz.msgs.Odometry',
                '/world/pendulum_world/model/pendulum_cart/joint_state@sensor_msgs/msg/JointState[gz.msgs.Model'
            ],
            output='screen'),
    ])
