import rclpy
from rclpy.node import Node
from demo_python_pkg.person_node import PersonNode

class WriterNode(PersonNode):
    def __init__(self,node_name:str,name:str,age:int,book:str) ->None:
        print('writer_node__init__被自动调用')
        super().__init__(node_name,name,age)#调用父类的__init__
        self.book = book
        #self.get_logger().info(f"{self.name},{self.age}岁，爱吃{food_name},发表{self.book}")

    #def eat(self,food_name: str):
    #        #print(f"{self.name},{self.age}岁，爱吃{food_name}")
    #        self.get_logger().info(f"{self.name},{self.age}岁，爱吃{food_name},发表{self.book}")




def main():
    rclpy.init()
    node =  WriterNode('writer_node','章三',18,'论存算一体')
    text = node.eat('面包', log_output=False)
    node.get_logger().info(f"{text}，发表《{node.book}》")
    rclpy.spin(node)
    rclpy.shutdown()
