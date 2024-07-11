#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from robot_tf_pkg.msg import encoder
from robot_tf_pkg.msg import motor
import numpy as np


def feedback(msg):
    motPub = rospy.Publisher('/motor_value', motor, queue_size=10)
    kinem = Twist()
    mot_val = motor()
    x = msg.linear.x
    y = -(msg.linear.y)
    z = (msg.angular.z)
    # z = 0

    matriks = np.array([[-0.33, 0.58, 0.33],
            [-0.33, -0.58, 0.33],
            [0.67, 0, 0.33]])
    pergerakan = np.array([y, x, z])

    hasil = np.dot(matriks, pergerakan)
    # hasil = np.dot(pergerakan, matriks)
 
    [mot1, mot2, mot3] = hasil

    mot1 = (mot1*255)/1
    mot2 = (mot2*255)/1
    mot3 = (mot3*255)/1

    mot1 = int(mot1)
    mot2 = int(mot2)
    mot3 = int(mot3)

    mot_val.motor1 = mot1
    mot_val.motor2 = mot2
    mot_val.motor3 = mot3
    # rospy.loginfo(mot_val.enc1)
    motPub.publish(mot_val)

    

if __name__ == '__main__':
    rospy.init_node('motor_process')
    # turtlename = rospy.get_param('~robot')
    rospy.Subscriber('/cmd_vel',Twist,feedback)
    rospy.spin()