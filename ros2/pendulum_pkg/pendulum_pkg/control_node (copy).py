#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from nav_msgs.msg import Odometry

class Control_Node(Node):
    def __init__(self):
        super().__init__("control_node")

        # Declare a param so you can choose the topic at launch/run time
        self.declare_parameter('odom_topic', '/model/pendulum_cart/odometry')
        topic = self.get_parameter('odom_topic').get_parameter_value().string_value

        self.create_subscription(Odometry, topic, self.get_odom, 10)
        self.get_logger().info(f"Subscribed to: {topic}")

    def get_odom(self, msg: Odometry):
        p = msg.pose.pose.position
        self.get_logger().info(f"[ODOM] x: {p.x:.2f}, y: {p.y:.2f}, z: {p.z:.2f}")

def main(args=None):
    rclpy.init(args=args)
    node = Control_Node()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()
