#! /usr/bin/env python

import rospy
from std_msgs.msg import Int32

rospy.init_node('simple_pub')
pub = rospy.Publisher('/counter',Int32,queue_size = 1)
rate = rospy.Rate(2)
count= Int32()
count.data = 0

while not rospy.is_shutdown():
    pub.publish(count.data)
    count.data +=1