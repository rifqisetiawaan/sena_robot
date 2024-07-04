#!/usr/bin/env python3

import math
from math import sin, cos, pi
import rospy
import tf
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Point, Pose, Quaternion, Twist, Vector3
from robot_tf_pkg.msg import encoder

# Initialize the ROS node
rospy.init_node('odometry_publisher')

# Publishers and Transform Broadcaster
odom_pub = rospy.Publisher("odom", Odometry, queue_size=50)
Robotpub = rospy.Publisher('robot_pos', Pose, queue_size=10)
odom_broadcaster = tf.TransformBroadcaster()
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
    float("{:.2f}".format(w1))
    float("{:.2f}".format(w2))
    float("{:.2f}".format(w3))

    # Convert wheel angular velocities to linear velocities
    v1 = w1 * wheel_radius
    v2 = w2 * wheel_radius
    v3 = w3 * wheel_radius

    # Convert wheel velocities to robot's linear and angular velocities
    vx = (2/3) * (v1 - 0.5 * v2 - 0.5 * v3)
    # vy = (1/math.sqrt(3)) * (v2 - v3)
    vth = ((1/(3 * robot_radius)) * (v1 + v2 + v3)) * 2
    derajat = math.radians(30)
    vy = v3 - (v2 * math.sin(derajat)) - (v1 *(math.sin(derajat)))
    # vx = (v1 * math.cos(derajat)) - (v2 * math.cos(derajat))

# Subscriber to encoder data
rospy.Subscriber("enco_value", encoder, encoder_callback)

# Main loop
r = rospy.Rate(10.0)
while not rospy.is_shutdown():
    current_time = rospy.Time.now()

    # Compute odometry in a typical way given the velocities of the robot
    dt = (current_time - last_time).to_sec()
    delta_x = (vx * cos(th) - vy * sin(th)) * dt
    delta_y = (vx * sin(th) + vy * cos(th)) * dt
    delta_th = vth * dt

    x += delta_x
    y += delta_y
    th += delta_th

    # Since all odometry is 6DOF we'll need a quaternion created from yaw
    odom_quat = tf.transformations.quaternion_from_euler(0, 0, th)

    # First, we'll publish the transform over tf
    odom_broadcaster.sendTransform(
        (x, y, 0.),
        odom_quat,
        current_time,
        "base_link",
        "odom"
    )

    # Next, we'll publish the odometry message over ROS
    odom = Odometry()
    odom.header.stamp = current_time
    odom.header.frame_id = "odom"

    # Set the position
    odom.pose.pose = Pose(Point(x, y, 0.), Quaternion(*odom_quat))

    # Set the velocity
    odom.child_frame_id = "base_link"
    odom.twist.twist = Twist(Vector3(vx, vy, 0), Vector3(0, 0, vth))
    rob_pos.position.x = x
    rob_pos.position.y = y

    # Publish the message
    Robotpub.publish(rob_pos)
    odom_pub.publish(odom)

    last_time = current_time
    r.sleep()