#! /usr/bin/env python

import rospy
import time
from sensor_msgs.msg import LaserScan
from nav_msgs.msg import Odometry

class Laser_topic():
    def __init__(self):
        self.sub = rospy.Subscriber('/kobuki/laser/scan', LaserScan, self.callback)
        self.ls = LaserScan()

    def callback(self, msg):
        self.ls = msg
        rospy.logdebug(self.ls)

    def get_data(self):
        return self.ls
    
    def laser_info(self, forward=0, left=0, right=0):
        self.forward = self.ls.ranges[360]
        self.left = self.ls.ranges[719]
        self.right = self.ls.ranges[0]
        return self.forward, self.right,self.left


class odom():

    def __init__(self):
        self.sub_odo = rospy.Subscriber('/odom', Odometry, self.my_callback_odom)
        self.odo = Odometry()

    def my_callback_odom(self,msg):
        self.odo = msg
        rospy,logdebug(self.odo)
            
    def get_data(self):
        return self.odo.header