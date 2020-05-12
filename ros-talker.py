#! /usr/bin/env python

import rospy
import time
from std_msgs.msg import Int32

rospy.init_node('talker_example_1')
pub = rospy.Publisher('counter_1', Int32)
count = 0

while not rospy.is_shutdown():
    pub.publish(count)
    count += 0.2
    time.sleep(1)
