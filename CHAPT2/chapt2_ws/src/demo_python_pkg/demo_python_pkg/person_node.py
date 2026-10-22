import rclpy
from rclpy.node import Node

class PersonNode(Node):
    def __init__(self,node_name:str,name_value: str,age_value: int) ->None:
        print('person_node__init__被自动调用')
        super().__init__(node_name)
        self.name = name_value
        self.age = age_value


    def eat(self, food_name: str, log_output: bool = True) -> str:
        text = f"{self.name}，{self.age}岁，喜欢吃{food_name}"
        if log_output:
            self.get_logger().info(text)
        return text


def main():
    rclpy.init()
    node =  PersonNode('zhangsan','章三',18)
    #node1 =  PersonNode('小王',45)
    node.eat('鸡腿')
    #node1.eat('鸡翅')
    rclpy.spin(node)
    rclpy.shutdown()