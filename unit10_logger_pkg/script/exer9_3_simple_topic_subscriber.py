#! /usr/bin/env python

import rospy
from std_msgs.msg import Int32

rospy.init_node('simple_sub')

def callback(msg):
    print(msg.data)
sub = rospy.Subscriber('/counter', Int32, callback)
rospy.spin()