#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist  # Change from Wrench to Twist

class Control_Node(Node):
    def __init__(self):
        super().__init__("control_node")
        # Change to VelocityControl topic
        self.cmd_pub = self.create_publisher(Twist, '/model/pendulum_cart/cmd_vel', 10)
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
        kp = 2.0  # Velocity control gain
        
        # Calculate velocity command
        velocity_y = kp * (target - y)

        cmd = Twist()
        cmd.linear.y = float(max(min(velocity_y, 3.0), -3.0))  # Limit velocity
        
        self.cmd_pub.publish(cmd)
        self.get_logger().info(f"Publishing velocity: {cmd.linear.y:.2f} m/s")

def main(args=None):
    rclpy.init(args=args)
    node = Control_Node()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()
