#!/usr/bin/env python3 
import rclpy 
from std_msgs.msg import Float32 
import random 
from rclpy.node import Node 

class UltrasonicSubsriberNode(Node): 
    def __init__(self) : 
        super().__init__("Ultrasonic_Subscriber") 
        self.SubsriberCreator=self.create_subscription(Float32,"ultrasonic_data",self.listener_callback,10)

    def listener_callback(self,msg) : 
        distance = msg.data 
        self.get_logger().info(f"the received distance is {distance}") 
        self.make_decision(distance)
    def make_decision(self,distance) : 
        if distance<10 : 
            self.get_logger().info("the object is too close ")
        elif distance <50 : 
            self.get_logger().info("the object is within range") 
        else : 
            self.get_logger().info("all clear ! ")


def main(args=None) : 
    rclpy.init(args=args) 
    node = UltrasonicSubsriberNode() 
    rclpy.spin(node) 
    rclpy.shutdown()