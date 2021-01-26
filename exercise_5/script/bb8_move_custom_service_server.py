#! /usr/bin/env python

import rospy
from exercise_5.srv import CustomSrvMsg, CustomSrvMsgResponse
from geometry_msgs.msg import Twist

def my_callback(request):
    my_response = CustomSrvMsgResponse()
    count = request.duration
    while count>0:
        move_bb8.linear.x = 0.5
        move_bb8.angular.z = 0.5
        pub.publish(move_bb8)
        count -= 1
        rospy.sleep(1)
    move_bb8.linear.x = 0
    move_bb8.angular.z = 0
    my_response.success = True    
    pub.publish(move_bb8)
    return my_response

rospy.init_node('service_server')
my_service = rospy.Service('/move_bb8_in_circle_custom',CustomSrvMsg,my_callback)
pub = rospy.Publisher('/cmd_vel',Twist,queue_size = 1)
move_bb8 = Twist()
rospy.spin()