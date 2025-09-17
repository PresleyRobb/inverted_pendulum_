#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
import numpy as np
from nav_msgs.msg import Odometry
from std_msgs.msg import Float64

class Control_Node(Node):
    def __init__(self):
        super().__init__("control_node")
        self.cmd_pub = self.create_publisher(Float64, '/model/pendulum_cart/joint/cart_slider/cmd_vel', 10)
        self.odom_sub = self.create_subscription(Odometry, '/model/pendulum_cart/odometry', self.get_odom, 10)

        
    def get_odom(self, msg):
        x = msg.pose.pose.position.x
        y = msg.pose.pose.position.y
        z = msg.pose.pose.position.z
        self.get_logger().info(f"[ODOM] x: {x:.2f}, y: {y:.2f}, z: {z:.2f}")
    
        self.move(msg)

    def move(self, msg):
        y = msg.pose.pose.position.y
        target = 5.0
        kp = 1.0
        v = kp * (target - y)

        cmd = Float64()
        cmd.data = float(max(min(v, 1.0), -1.0))
        self.cmd_pub.publish(cmd)
	    
	    

def main(args=None):
    rclpy.init(args=args)
    node = Control_Node()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()
