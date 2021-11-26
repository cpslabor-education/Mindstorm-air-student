import rclpy
from rclpy.node import Node
from rcl_interfaces import msg
from rosidl_parser.definition import BOOLEAN_TYPE
# from std_msgs.msg import Int32, Float32
from geometry_msgs.msg import Vector3


class UserInputNode(Node):

    def __init__(self):
        super().__init__("user_input_node")
        # Subscriber
        self.sub_need_input = self.create_subscription(bool, "need_input_topic", self.CB_NeedInput_Topic, 0)
        # Publisher
        self.pub_input_command = self.create_publisher(Vector3, 'input_command_topic', 0)
        # Init kész üzenet
        self.get_logger().info("[User Input node] init done.")

    def GetUserInput(self):
        distance = 'Wrong input!'
        while type(distance) is not int and type(distance) is not float:
            distance = input('Enter distance: ')
        #Itt lehet még bekérni adatokat a már leírt minta szerint.

        return distance

    def CB_NeedInput_Topic(self, data: bool):
        if data == True:
            user_input = self.GetUserInput()
            motor_commands = Vector3()
            motor_commands.x = None
            motor_commands.y = None
            motor_commands.z = None
            """
            A user_input egy egész, vagy float típusú szám lesz,
            amit a konzolból kér be a felhasználótól.
            Ez a szám jelenleg arra hivatott,
            hogy megmondja mennyit menjen egy irányba.
            Ha szükség van mégtöbb számra, akkor azt találd ki nekem légyszi.
            Ezek alapján a bekért számok alapján
            valami mozgási viselkedést kellene alkotni.
            Bal és jobb motor meghajtás van, amiknek sebességet tudunk adni.
            A sebességet rá lehet adni bizonyos ideig, vagy bizonyos fordulatig, stb.
            A bekért számokat kellene valamilyen függvény/rendszer szerint átalakítani úgy,
            hogy a motorvezérlő parancsba beilleszthető számok legyenek belőle.
            A motor_commands nevű változóba mentsd el, amit a motorba kell majd küldeni.
            Ez a változó Vector3 típusú, ami azt jelenti, hogy x, y, z elemei vannak.
            x = bal motor sebesség
            y = jobb motor sebesség
            z = mennyi ideig menjenek
            Fentebb láthatod, hogy hogyan kell értéket adni az elemeinek.
            Ennek a hosszú kommentnek helyére írd a kódodat!
            """
            self.pub_input_command.publish(motor_commands)
        else:
            return None


def main(args = None):
    rclpy.init(args=args)
    user_input_node = UserInputNode()
    rclpy.spin(user_input_node)
    user_input_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
