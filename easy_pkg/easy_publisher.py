import rclpy
from rclpy.node import Node

from std_msgs.msg import String

class EasyPublisher(Node):

    def __init__(self):
        super().__init__('easy_publisher')
        self.publisher_ = self.create_publisher(String, 'words', 10)
        # timer_period = 0.5
        # self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0
        self.prompt_user()

    def prompt_user(self):
        user_input = ""
        msg = String()

        while user_input != "quit":
            user_input = input("-> ")

            msg.data = user_input

            self.publisher_.publish(msg)
            self.get_logger().info('Publishing: "%s"' % msg.data)
            self.i += 1

def main(args=None):
    rclpy.init(args=args)

    easy_publisher = EasyPublisher()

    rclpy.spin(easy_publisher)

    easy_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
