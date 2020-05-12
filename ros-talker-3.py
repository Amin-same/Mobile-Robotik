#! /usr/bin/env python

import rospy
import time
from std_msgs.msg import Float32

rospy.init_node('talker_example_3')
pub = rospy.Publisher('counter_3', Float32)
myFloat = 0

while not rospy.is_shutdown():
    pub.publish(myFloat)
    myFloat+=0.1
    time.sleep(1)
