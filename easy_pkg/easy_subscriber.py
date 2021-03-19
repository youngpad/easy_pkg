import rclpy
from rclpy.node import Node

from std_msgs.msg import String

class EasySubscriber(Node):

    def __init__(self):
        super().__init__('easy_subscriber')
        self.subscription = self.create_subscription(String, 'words', self.listener_callback, 10)
        self.subscription
        self.i = 0

    def listener_callback(self, msg):
        self.get_logger().info('I heard: "%s"' % msg.data)

def main(args=None):
    rclpy.init(args=args)

    easy_subscriber = EasySubscriber()

    rclpy.spin(easy_subscriber)

    easy_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
