#! /usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

class moveTurtlebot():

    def __init__(self):
        self.move = Twist()
        self.pub = rospy.Publisher('/cmd_vel', Twist, queue_size = 1)

    def move_speed(self,linear_speed, angular_speed):
        self.linear_speed = linear_speed
        self.angular_speed = angular_speed
    
    def move_turtle(self, direction):
        if direction == "forwards":
            self.move.linear.x = self.linear_speed
            self.move.angular.z = 0.0
        if direction == "right":
            self.move.linear.x = 0.0
            self.move.angular.z = -self.angular_speed
        if direction == "left":
            self.move.linear.x = 0.0
            self.move.angular.z = self.angular_speed
        if direction == "backwards":
            self.move.linear.x = -self.linear_speed
            self.move.angular.z = 0.0
        if direction == "stop":
            self.move.linear.x = 0.0
            self.move.angular.z = 0.0
        self.pub.publish(self.move)




