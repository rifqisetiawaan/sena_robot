#!/usr/bin/env python3
import rospy
import tf2_ros
import tf.transformations as tf
import tf2_geometry_msgs  # For quaternion conversions
from geometry_msgs.msg import Pose, PoseStamped
import geometry_msgs
from robot_tf_pkg.msg import encoder
import math

def handle_robot_pose(msg):
    global xpos, ypos
    xpos = msg.position.x
    ypos = msg.position.y

def handle_ball_pose(msg, turtlename):
    global xpos, ypos
    br = tf2_ros.TransformBroadcaster()
    t = geometry_msgs.msg.TransformStamped()
    posBall = PoseStamped()

    xball = msg.position.x/100
    yball = msg.position.y/100
    
    # Adjust coordinates
    x = xball
    y = yball
    # x = (msg.position.x / 100)
    # y = (msg.position.y / 100)

    # Rotate coordinates by 90 degrees counterclockwise
    x_rotated = y
    y_rotated = x

    if msg.position.x == 0 and msg.position.y == 0:
        t.header.stamp = rospy.Time.now()
        t.header.frame_id = "camera_link"
        t.child_frame_id = "balls"
        t.transform.translation.x = 0.0
        t.transform.translation.y = 0.0
        t.transform.translation.z = 0.0
        t.transform.rotation.x = 0
        t.transform.rotation.y = 0
        t.transform.rotation.z = 0
        t.transform.rotation.w = 1
        
        # posBall.header.frame_id = 'map'
        # posBall.header.stamp = rospy.Time.now()
        # posBall.pose.position.x = xpos
        # posBall.pose.position.y = ypos
        # posBall.pose.position.z = 0.0
        # posBall.pose.orientation.x = 0
        # posBall.pose.orientation.y = 0
        # posBall.pose.orientation.z = 0
        # posBall.pose.orientation.w = 1
        # ball_pub.publish(posBall)
    else:
        t.header.stamp = rospy.Time.now()
        t.header.frame_id = "camera_link"
        t.child_frame_id = "balls"
        t.transform.translation.x = x_rotated
        t.transform.translation.y = y_rotated
        t.transform.translation.z = 0.0
        t.transform.rotation.x = 0
        t.transform.rotation.y = 0
        t.transform.rotation.z = 0
        t.transform.rotation.w = 1
        
        # posBall.header.frame_id = 'map'
        # posBall.header.stamp = rospy.Time.now()
        # posBall.pose.position.x = x_rotated
        # posBall.pose.position.y = y_rotated
        # posBall.pose.position.z = 0.0
        # posBall.pose.orientation.x = 0
        # posBall.pose.orientation.y = 0
        # posBall.pose.orientation.z = 0
        # posBall.pose.orientation.w = 1
        # ball_pub.publish(posBall)
        
    br.sendTransform(t)

def main():
    rospy.init_node('tf2_ball_broadcaster')
    turtlename = rospy.get_param('~balls')
    rospy.Subscriber('ballPos_topic', Pose, handle_ball_pose, turtlename)
    rospy.Subscriber('robot_pos', Pose, handle_robot_pose)
    rospy.spin()

if __name__ == '__main__':
    main()