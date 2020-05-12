#! /usr/bin/env python

import rospy
import time
from std_msgs.msg import Int32

rospy.init_node('listener_example_1')

def callback(msg):
    print msg.data

sub = rospy.Subscriber('counter_1', Int32, callback)
rospy.spin()
