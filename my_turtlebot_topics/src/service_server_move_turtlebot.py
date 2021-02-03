#! /usr/bin/env python

import rospy
from std_srvs.srv import Trigger, TriggerResponse
from my_turtlebot_topic import moveTurtlebot
from laser_topic_turtlebot import Laser_topic, odom
import time

rospy.init_node('service_serv')
def my_callback(request):
    turt = moveTurtlebot()
    my_response = TriggerResponse()
    las = Laser_topic()
    count = 5
    rospy.sleep(1)
    print(las.laser_info())
    x,y,z = las.laser_info()
    while x>1.4:
        turt.move_speed(1,0.5)
        turt.move_turtle('forwards')
        x,y,z = las.laser_info()
        print(x,y,z)
        rospy.sleep(0.5)
    turt.move_speed(0,0)
    turt.move_turtle('stop')
    x,y,z = las.laser_info()
    print(x,y,z)
    rospy.sleep(1)
    if y>1.5:
        my_response.message = 'Its about to hit obstacle, Move right'
    else:
        my_response.message = 'Its about to hit obstacle, Move left'       
    rospy.sleep(1)
    my_response.success = True
    return my_response

my_service = rospy.Service('/obstacle', Trigger, my_callback)
rospy.spin()

