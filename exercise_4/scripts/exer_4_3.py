#! /usr/bin/env python

import rospy
from exercise_4.msg import Age

rospy.init_node('age_robot')
pub = rospy.Publisher('/age',Age, queue_size=1)
rate = rospy.Rate(2)
var = Age()
var.years
var.months
var.days

while not rospy.is_shutdown(): 
  pub.publish(var)
  rate.sleep()