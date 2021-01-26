#! /usr/bin/env python

import rospy
from std_srvs.srv import Empty, EmptyResponse
from geometry_msgs.msg import Twist

def my_callback(request):
    move_bb8.linear.x = 0.5
    move_bb8.angular.z = 0.5
    pub.publish(move_bb8)
    return EmptyResponse()

rospy.init_node('service_server')
my_service = rospy.Service('/move_bb8_in_circle',Empty,my_callback)
pub = rospy.Publisher('/cmd_vel',Twist,queue_size = 1)
move_bb8 = Twist()
rospy.spin()