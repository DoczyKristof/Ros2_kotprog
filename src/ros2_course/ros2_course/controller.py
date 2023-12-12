import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

class MoveTurtlebotNode(Node):
    def __init__(self):
        super().__init__('controller')
        self.publisher = self.create_publisher(Twist, '/cmd_vel', 10)
        self.subscription = self.create_subscription(
            LaserScan,
            '/scan',
            self.listener_callback,
            10)
        self.msg = Twist()

    '''
    front_distance, front_right_distance, front_left_distance = 500.0, 500.0, 500.0    
    
    def checkFrontValues():
        return front_distance < treshold or front_right_distance < treshold or front_left_distance < treshold
    '''
    
    def listener_callback(self, msg):
        treshold = 0.8
        ranges = msg.ranges
        front_distance = ranges[0]
        front_right_distance = ranges[5]
        front_left_distance = ranges[-5]
        self.get_logger().info('range ahead: "%s"' % front_distance)
        if front_distance < treshold or front_right_distance < treshold or front_left_distance < treshold:
            self.msg.linear.x = 0.0
            self.msg.angular.z = 2.5
        else:
            self.msg.linear.x = 0.5
            self.msg.angular.z = 0.0
        self.publisher.publish(self.msg)

def main(args=None):
    rclpy.init(args=args)

    controller = MoveTurtlebotNode()

    rclpy.spin(controller)

    controller.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
