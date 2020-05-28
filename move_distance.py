#!/usr/bin/env python

import rospy
import time
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import sys


robot_x = 0
def pose_callback(pose):
    global robot_x
    rospy.loginfo("Robot X = %f\n", pose.x)
    robot_x = pose.x

vel = Twist()
rPose = Pose()
robot_x = rPose.x

rospy.Subscriber('/turtle1/pose', Pose, pose_callback)


def move_turtle(lin_vel, ang_vel, distance):
    global robot_x
    passedDistance = 0
    rospy.init_node('move_turtle', anonymous=False)
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(10)  # 10hz

    vel.linear.x = lin_vel
    vel.linear.y = 0
    vel.linear.z = 0
    vel.angular.x = 0
    vel.angular.y = 0
    vel.angular.z = ang_vel

    while not rospy.is_shutdown():
        t = time.time()
        # do stuff

        rospy.loginfo("Distance = %f, robot_x = %f\n", distance, robot_x)


        pub.publish(vel)

        if distance <= passedDistance:
            rospy.loginfo("Robot Reached destination")
            rospy.logwarn("Stopping robot")
            break
        elapsed = time.time() - t
        passedDistance = passedDistance + elapsed*abs(lin_vel)
        #rate.sleep()

move_turtle(-1,0,2)
move_turtle(0,-1.9,0)
time.sleep(1)
move_turtle(1,0,4)
move_turtle(0,-1.24,0)
time.sleep(1)
move_turtle(1,0,1)
move_turtle(0,-1.9,0)
time.sleep(1)
move_turtle(1,0,8)
move_turtle(0,-1.2,0)
time.sleep(1)
move_turtle(1,0,1.2)
move_turtle(0,-1.24,0)
time.sleep(1)
move_turtle(1,0,8)
move_turtle(0,-1.9,0)
time.sleep(1)
move_turtle(1,0,1)
move_turtle(0,-1.2,0)
time.sleep(1)
move_turtle(1,0,6.7)
move_turtle(0,2.4,0)
time.sleep(1)
move_turtle(1,0,1.5)
move_turtle(0,1.9,0)
time.sleep(1)
move_turtle(1,0,0.3)
time.sleep(1)
move_turtle(0,2.2,0)
time.sleep(1)