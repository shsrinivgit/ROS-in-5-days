#! /usr/bin/env python
import rospy

import actionlib
from actionlib.msg import TestAction, TestActionResult, TestActionFeedback
from geometry_msgs.msg import Twist
from std_msgs.msg import Empty

class SquareClass(object):
    
    
  # create messages that are used to publish feedback/result
  _feedback = TestActionFeedback()
  _result   = TestActionResult()

  def __init__(self):
    # creates the action server
    self._as = actionlib.SimpleActionServer("drone_sqr", TestAction, self.goal_callback, False)
    self._as.start()
    

  def goal_callback(self, goal):
    # this callback is called when the action server is called.

    # and returns the sequence to the node that called the action server
    r = rospy.Rate(1)
    self.pub = rospy.Publisher('/cmd_vel', Twist,queue_size = 1)
    self.pub2 = rospy.Publisher('drone/takeoff', Empty,queue_size = 1)
    self.takeoff = Empty()
    self.pub3 = rospy.Publisher('drone/land', Empty, queue_size = 1)
    self.landing = Empty()
    self.move_drone = Twist()
    self.x = 0.3
    self.y = 0.3 
    self.count = 1
    self.sqr = 2
    success = True

    x = rospy.get_rostime()
    SquareOrder = self.count
    while SquareOrder>0:
      # check that preempt (cancelation) has not been requested by the action client
        if self._as.is_preempt_requested():
            rospy.loginfo('The goal has been cancelled/preempted')
        # the following line, sets the client in preempted state (goal cancelled)
            self._as.set_preempted()
            success = False
            break

        square= self.sqr # get the square value for 2 sides 
        self._feedback.feedback = 1 #set the initial value for feedback
        while square > 0:
            cnt = goal.goal #get the no of secs to do one side of the square
            while cnt>0: # for value x
                self.pub2.publish(self.takeoff) 
                self.move_drone.linear.x = self.x
                self.pub.publish(self.move_drone)
                rospy.sleep(1)
                self._as.publish_feedback(self._feedback)
                cnt -=1

            cnt = goal.goal
            self._feedback.feedback +=1
            while cnt>0: #for value y
                self.move_drone.linear.y = self.y
                self.move_drone.linear.x = 0
                self.pub.publish(self.move_drone)
                rospy.sleep(1)
                self._as.publish_feedback(self._feedback)
                cnt -=1
            #make the 
            self._feedback.feedback +=1   
            self.move_drone.linear.y = 0
            self.pub.publish(self.move_drone)
            self.x = -self.x
            self.y = -self.y
            square -= 1
        SquareOrder -= 1
        #perform the square 
        print('Square',SquareOrder)
    self.move_drone.linear.x = 0
    self.move_drone.angular.z = 0
    self.pub.publish(self.move_drone)
    self.pub3.publish(self.landing)
    # at this point, either the goal has been achieved (success==true)
    # or the client preempted the goal (success==false)
    # If success, then we publish the final result
    # If not success, we do not publish anything in the result
    if success:
      self._result.result = self._feedback.feedback *2*self.sqr
      rospy.loginfo('Total spent time moving the drone %d' % self._result.result )
      self._as.set_succeeded(self._result)
if __name__ == '__main__':
  rospy.init_node('drone_square')
  SquareClass()
  rospy.spin()