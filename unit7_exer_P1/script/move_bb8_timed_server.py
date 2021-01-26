#! /usr/bin/env python

import rospy
from exercise_5.srv import CustomSrvMsg, CustomSrvMsgResponse
from move_bb8_timed import MoveBB8

def my_callback(request):
    rospy.loginfo("The Service move_bb8_in_circle has been called")
    my_response = CustomSrvMsgResponse()
    movebb8_object = MoveBB8()
    movebb8_object.move_bb8(request.duration)
    rospy.loginfo("Finished service move_bb8_in_circle")
    my_response.success = True
    return my_response 

rospy.init_node('service_move_bb8_in_circle_server') 
my_service = rospy.Service('/move_bb8_in_circle_custom', CustomSrvMsg , my_callback)
rospy.loginfo("Service /move_bb8_in_circle_custom Ready")
rospy.spin() # mantain the service open.