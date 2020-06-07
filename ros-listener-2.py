#! /usr/bin/env python

import rospy
import time
from std_msgs.msg import String

rospy.init_node('listener_example_2')

def callback(msg):
    print msg.data

sub = rospy.Subscriber('counter_2', String, callback)
rospy.spin()
