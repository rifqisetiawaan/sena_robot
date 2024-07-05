#!/usr/bin/env python3
import rospy
import tf2_ros
from geometry_msgs.msg import PoseStamped, TransformStamped

def publish_base_link_pose():
    rospy.init_node('base_link_pose_publisher')
    tf_buffer = tf2_ros.Buffer()
    listener = tf2_ros.TransformListener(tf_buffer)
    pose_pub = rospy.Publisher('base_link_pose', PoseStamped, queue_size=10)

    rate = rospy.Rate(10.0)
    while not rospy.is_shutdown():
        try:
            # Lookup transform from 'odom' to 'base_link'
            trans = tf_buffer.lookup_transform('odom', 'base_link', rospy.Time())

            # Create PoseStamped message
            pose_msg = PoseStamped()
            pose_msg.header.stamp = rospy.Time.now()
            pose_msg.header.frame_id = 'odom'  # Frame of the pose
            pose_msg.pose.position.x = trans.transform.translation.x
            pose_msg.pose.position.y = trans.transform.translation.y
            pose_msg.pose.position.z = trans.transform.translation.z
            pose_msg.pose.orientation.x = trans.transform.rotation.x
            pose_msg.pose.orientation.y = trans.transform.rotation.y
            pose_msg.pose.orientation.z = trans.transform.rotation.z
            pose_msg.pose.orientation.w = trans.transform.rotation.w

            # Publish PoseStamped message
            pose_pub.publish(pose_msg)

        except (tf2_ros.LookupException, tf2_ros.ConnectivityException, tf2_ros.ExtrapolationException) as e:
            rospy.logwarn("Exception occurred: %s", e)

        rate.sleep()

if __name__ == '__main__':
    try:
        publish_base_link_pose()
    except rospy.ROSInterruptException:
        pass
