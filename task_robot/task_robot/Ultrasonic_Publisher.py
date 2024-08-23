#!/usr/bin/env python3 
import rclpy 
from rclpy.node import Node 
from std_msgs.msg import Float32 
import random 


class UltrasonicPublisherNode(Node) : 
    def __init__(self) : 
        super().__init__("Ultrasonic_Publisher") 
        self.PublsihCreator=self.create_publisher(Float32,"ultrasonic_data",10)
        self.timer_=self.create_timer(0.1,self.publishData)

    def publishData(self) : 
        estimated_distance=random.uniform(0.0,100.0)
        msg=Float32() 
        msg.data=estimated_distance
        self.PublsihCreator.publish(msg)
        self.get_logger().info(f"the estimated distance is {estimated_distance}")

def main(args=None) : 
    rclpy.init(args=args) 
    node=UltrasonicPublisherNode()
    rclpy.spin(node)
    rclpy.shutdown()