import rclpy
from rclpy.node import Node
from rcl_interfaces import msg
# from std_msgs.msg import Int32
from geometry_msgs.msg import Vector3


class MotorsNode(Node):

    def __init__(self):
        super().__init__("motors_node")
        # Subscriber
        self.sub_input_command = self.create_subscription(Vector3, 'input_command_topic', self.CB_InputCommand_Topic, 0)
        # Publisher
        self.pub_need_input = self.create_publisher(bool, 'need_input_topic', 0)
        # Init kész üzenet
        self.get_logger().info("[Motors Node] init done.")

    def MoveDone(self, movetype: str):
        self.get_logger().info(movetype, "movement is done.")

    def CB_InputCommand_Topic(self, data: Vector3):
        motor_commands = data

        # Motor vezérlő parancsok
        # x = bal motor sebesség
        # y = jobb motor sebesség
        # z = mennyi ideig menjenek

        # Feltételvizsgálat és mozgás utáni teendők
        if True:
            self.MoveDone("Manual")
            # Jöhet az új parancs
            self.pub_need_input.publish(True)
        else:
            # Nem kell még új parancs
            self.pub_need_input.publish(False)


    

def main(args = None):
    rclpy.init(args=args)
    motors_node = MotorsNode()
    rclpy.spin(motors_node)
    motors_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
