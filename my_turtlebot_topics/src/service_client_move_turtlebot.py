#! /usr/bin/env python

import rospy
# Import the service message used by the service /trajectory_by_name
from std_srvs.srv import Trigger, TriggerRequest
from geometry_msgs.msg import Twist
import sys
# Initialise a ROS node with the name service_client
rospy.init_node('service_cli')
# Wait for the service client //execute_trajectory to be running
rospy.wait_for_service('/obstacle')
# Create the connection to the service
move_turtbot_service = rospy.ServiceProxy('/obstacle', Trigger)
# Create an object of type TriggerRequest
move_turbot_object = TriggerRequest()
# Send through the connection the name of the trajectory to be executed by the robot
result = move_turtbot_service(move_turbot_object)
# Print the result given by the service called
print(result)