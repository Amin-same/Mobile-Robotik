#!/usr/bin/env python
import rospy
import time
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import sys

def pose_callback(pose):
	rospy.loginfo("Robot X = %f : Y=%f : Theta=%f\n",pose.x,pose.y,pose.theta)

# Starts a new node
rospy.init_node('robot_cleaner', anonymous=False)

velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)

rate = rospy.Rate(100)

vel_msg = Twist()

delay = input("Input the delay: ")

rospy.Subscriber('/turtle1/pose', Pose, pose_callback)

vel_msg.linear.x = 0
vel_msg.linear.y = 0
vel_msg.linear.z = 0
vel_msg.angular.x = 0
vel_msg.angular.y = 0
vel_msg.angular.z = 1

while not rospy.is_shutdown():
    velocity_publisher.publish(vel_msg)
    time.sleep(delay)
    rate.sleep()
