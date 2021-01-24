#! /usr/bin/env python

import rospy
from nav_msgs.msg import Odometry

def callback(msg): 
  print msg.header.stamp
  print msg.pose.pose.position.x
  print msg.twist
  print msg.pose.pose.orientation

rospy.init_node('robot_odometry')
sub = rospy.Subscriber('/odom', Odometry, callback)
rospy.spin()