#!/usr/bin/env python

import rospy
import tf2_ros
import tf2_geometry_msgs
from geometry_msgs.msg import PoseStamped

def publish_goal():
    rospy.init_node('goal_publisher')
    
    tf_buffer = tf2_ros.Buffer()
    listener = tf2_ros.TransformListener(tf_buffer)
    
    goal_pub = rospy.Publisher('/move_base_simple/goal', PoseStamped, queue_size=10)
    
    rate = rospy.Rate(10.0)
    while not rospy.is_shutdown():
        try:
            # Look up the transform from camera_link to map
            trans = tf_buffer.lookup_transform('map', 'balls', rospy.Time(0))

            # Create a goal in camera_link frame
            goal_in_camera_frame = PoseStamped()
            goal_in_camera_frame.header.frame_id = 'balls'
            goal_in_camera_frame.header.stamp = rospy.Time.now()
            goal_in_camera_frame.pose.position.x = 0.0  # Example goal coordinates
            goal_in_camera_frame.pose.position.y = 0.0
            goal_in_camera_frame.pose.position.z = 0.0
            goal_in_camera_frame.pose.orientation.w = 1.0

            # Transform the goal to map frame
            goal_in_map_frame = tf2_geometry_msgs.do_transform_pose(goal_in_camera_frame, trans)

            # Publish the goal
            goal_pub.publish(goal_in_map_frame)

        except (tf2_ros.LookupException, tf2_ros.ConnectivityException, tf2_ros.ExtrapolationException):
            continue

        rate.sleep()

if __name__ == '__main__':
    try:
        publish_goal()
    except rospy.ROSInterruptException:
        pass