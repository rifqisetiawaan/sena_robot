#!/usr/bin/env python3

import math
import rospy
import tf2_ros
import tf
import tf2_geometry_msgs  # Untuk konversi quaternion
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Point, Pose, Quaternion, Twist, Vector3
from robot_tf_pkg.msg import encoder
import geometry_msgs
import numpy as np

# Initialize the ROS node
rospy.init_node('odometry_publisher')

# Publishers and Transform Broadcaster
odom_pub = rospy.Publisher("odom", Odometry, queue_size=50)
Robotpub = rospy.Publisher('robot_pos', Pose, queue_size=10)
tf_buffer = tf2_ros.Buffer()
tf_listener = tf2_ros.TransformListener(tf_buffer)
odom_broadcaster = tf2_ros.TransformBroadcaster()
rob_pos = Pose()

# Initialize position and orientation
x = 0.0
y = 0.0
th = 0.0

# Initialize velocities
vx = 0.0
vy = 0.0
vth = 0.0

# Wheel radius and distance from the center to the wheel
wheel_radius = 0.05  # 50 mm converted to meters
robot_radius = 0.218   # This should be set to your robot's actual radius

# Time management
current_time = rospy.Time.now()
last_time = rospy.Time.now()

# Callback function to handle encoder data
def encoder_callback(data):
    global vx, vy, vth
    # Get the velocities of each wheel (in rad/s)
    w1 = data.enc1
    w2 = data.enc2
    w3 = data.enc3

    # Convert wheel angular velocities to linear velocities
    v1 = w1 * wheel_radius
    v2 = w2 * wheel_radius
    v3 = w3 * wheel_radius

    # Convert wheel velocities to robot's linear and angular velocities
    # vx = (2/3) * (v1 - 0.5 * v2 - 0.5 * v3)
    # vx = (v1 * math.cos(math.radians(30))) - (v2 * math.cos(math.radians(30)))
    vx = (v1-v2)/np.sqrt(3)
    vy = (v1 + v2 - 2 * v3) / 3
    vth = ((v1 / robot_radius) + (v2 / robot_radius) + (v3 / robot_radius))/3

# Subscriber to encoder data
rospy.Subscriber("enco_value", encoder, encoder_callback)

# Main loop
r = rospy.Rate(10.0)
while not rospy.is_shutdown():
    current_time = rospy.Time.now()

    # Compute odometry in a typical way given the velocities of the robot
    dt = (current_time - last_time).to_sec()
    delta_x = (vx * math.cos(th) - vy * math.sin(th)) * dt
    delta_y = (vx * math.sin(th) + vy * math.cos(th)) * dt
    delta_th = vth * dt

    x += delta_x
    y += delta_y
    th += delta_th

    # Since all odometry is 6DOF we'll need a quaternion created from yaw
    odom_quat = Quaternion(*tf.transformations.quaternion_from_euler(0, 0, th))

    # First, we'll publish the transform over tf2
    transform_stamped = geometry_msgs.msg.TransformStamped()
    transform_stamped.header.stamp = current_time
    transform_stamped.header.frame_id = "odom"
    transform_stamped.child_frame_id = "base_link"
    transform_stamped.transform.translation.x = x
    transform_stamped.transform.translation.y = y
    transform_stamped.transform.translation.z = 0.0
    transform_stamped.transform.rotation = odom_quat
    odom_broadcaster.sendTransform(transform_stamped)

    # Next, we'll publish the odometry message over ROS
    odom = Odometry()
    odom.header.stamp = current_time
    odom.header.frame_id = "odom"

    # Set the position
    odom.pose.pose = Pose(Point(x, y, 0.), odom_quat)
    rob_pos.position.x = x
    rob_pos.position.y = y
    rob_pos.orientation = odom_quat

    # Set the velocity
    odom.child_frame_id = "base_link"
    odom.twist.twist = Twist(Vector3(vx, vy, 0), Vector3(0, 0, vth))
    transform_stamped.header.stamp = rospy.Time.now()
    transform_stamped.header.frame_id = "base_link"
    transform_stamped.child_frame_id = "camera_link"
    transform_stamped.transform.translation.x = 0.0
    transform_stamped.transform.translation.y = 0.0
    transform_stamped.transform.translation.z = 0.0
    # q = tf_conversions.transformations.quaternion_from_euler(0, 0, msg.theta)
    transform_stamped.transform.rotation.x = 0
    transform_stamped.transform.rotation.y = 0
    transform_stamped.transform.rotation.z = 0
    transform_stamped.transform.rotation.w = 1


    # Publish the message
    Robotpub.publish(rob_pos)
    odom_pub.publish(odom)

    last_time = current_time
    r.sleep()

rospy.spin()