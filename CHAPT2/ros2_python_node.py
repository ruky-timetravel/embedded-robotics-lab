import rclpy
from rclpy.node import Node

def main():
    rclpy.init() # 初始化工作，分配资源
    node = Node('python_node')
    node.get_logger().info('你好')
    node.get_logger().warning('你好')
    rclpy.spin(node)
    rclpy.shutdown()

if __name__=='__main__':
    main()
