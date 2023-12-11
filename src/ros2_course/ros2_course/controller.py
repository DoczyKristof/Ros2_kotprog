import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

class MoveTurtlebotNode(Node):
    def __init__(self):
        super().__init__('moveturtlebot')
        self.publisher = self.create_publisher(Twist, '/cmd_vel', 10)
        self.subscription = self.create_subscription(
            LaserScan,
            '/scan',
            self.listener_callback,
            10)
        self.msg = Twist()

    def listener_callback(self, msg):
        range_ahead = msg.ranges[-1]  #forward range
        self.get_logger().info('range ahead: "%s"' % range_ahead)
        if range_ahead < 0.25:
            self.msg.linear.x = 0.0
            self.msg.angular.z = 0.5
        else:
            self.msg.linear.x = 0.25
            self.msg.angular.z = 0.0
        self.publisher.publish(self.msg)

def main(args=None):
    rclpy.init(args=args)

    move_turtlebot_node = MoveTurtlebotNode()

    rclpy.spin(move_turtlebot_node)

    move_turtlebot_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
