#!/usr/bin/env python3
import rclpy
import numpy as np
from rclpy.node import Node
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist
from sensor_msgs.msg import JointState

class Control_Node(Node):
    def __init__(self):
        super().__init__("control_node")
        #publishers
        self.cmd_pub = self.create_publisher(Twist, '/model/pendulum_cart/cmd_vel', 10)
        #subscribers
        self.odom_sub = self.create_subscription(Odometry, '/model/pendulum_cart/odometry', self.get_odom, 10)
        self.joint_sub = self.create_subscription(JointState, '/world/pendulum_world/model/pendulum_cart/joint_state', self.joint_state_callback, 10)
        #state variables
        self.m = 0.1     #pendulum mass
        self.M = 1.0    #cart mass
        self.L= 0.375   #pendulum lenght
        self.k = 0      #cart friction coeffients(unclear on how to calculate this)
        self.v = 0.002  #pendulum friction
        self.theta = 0.0    #pendulum angle
        self.y = 0.0    #cart position
        self.theta_dot = 0.0    #pendulum velocity
        self.y_dot = 0  #cart velocity
        self.target_position = 0.0  # Added missing variable
        
    def joint_state_callback(self, msg):
        try:
            idx = msg.name.index('pendulum_pivot')
            self.theta = msg.position[idx]      
            self.theta_dot = msg.velocity[idx]
        
            self.get_logger().info(
                f"[PENDULUM] θ: {self.theta:.3f} rad ({np.degrees(self.theta):.1f}°), "
                f"θ̇: {self.theta_dot:.3f} rad/s",
                throttle_duration_sec=1.0
            )
        except (ValueError, IndexError):
            pass

    def get_odom(self, msg):
        # Update cart position and velocity
        self.y = msg.pose.pose.position.y
        self.y_dot = msg.twist.twist.linear.y
    
        x = msg.pose.pose.position.x
        z = msg.pose.pose.position.z
    
        self.get_logger().info(
            f"[CART] y: {self.y:.2f}m, ẏ: {self.y_dot:.2f}m/s"
        )
        self.move()

    def move(self):
        kp = 1.0
        velocity_y = kp * (self.target_position - self.y)
    
        cmd = Twist()
        cmd.linear.y = float(max(min(velocity_y, 3.0), -3.0))
    
        self.cmd_pub.publish(cmd)

def main(args=None):
    rclpy.init(args=args)
    node = Control_Node()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()
