#!/usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

class ObstacleAvoidance:
    def __init__(self):
        rospy.init_node('obstacle_avoidance')
        self.pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        self.sub = rospy.Subscriber('/scan', LaserScan, self.callback)
        self.msg = Twist()

    def callback(self, data):
        front = min(min(data.ranges[0:15] + data.ranges[-15:]), 10)
        if front < 0.5:
            self.msg.linear.x = 0.0
            self.msg.angular.z = 0.5  # Turn
        else:
            self.msg.linear.x = 0.2
            self.msg.angular.z = 0.0
        self.pub.publish(self.msg)

if __name__ == '__main__':
    try:
        ObstacleAvoidance()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
