#! /usr/bin/env python

import rospy
import time
from std_msgs.msg import String

rospy.init_node('talker_example_2')
pub = rospy.Publisher('counter_2', String)
myChar = "Hallo"

while not rospy.is_shutdown():
    pub.publish(myChar)
    time.sleep(1)
