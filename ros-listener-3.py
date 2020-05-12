#! /usr/bin/env python

import rospy
import time
from std_msgs.msg import Float32


rospy.init_node('listener_example_3')

def callback(msg):
    print msg.data

sub = rospy.Subscriber('counter_3', Float32, callback)
rospy.spin()
