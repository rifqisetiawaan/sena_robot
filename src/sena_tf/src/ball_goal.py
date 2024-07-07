#!/usr/bin/env python3
import rospy
import tf
import tf2_ros
import tf2_geometry_msgs  # For quaternion conversions
from geometry_msgs.msg import Pose, PoseStamped
import geometry_msgs
from robot_tf_pkg.msg import encoder
import math
import numpy as np

ball_pub = rospy.Publisher('/move_base_simple/goal', PoseStamped, queue_size=10)

def handle_robot_pose(msg):
    xpos = msg.position.x
    ypos = msg.position.y
    theta = msg.orientation
    theta = tf.transformations.euler_from_quaternion(theta)
    return xpos, ypos, theta

def handle_ball_pose(msg):    
    # Adjust coordinates cm -> m
    x = (msg.position.x / 100)
    y = (msg.position.y / 100)

    # Rotate coordinates by 90 degrees counterclockwise
    x_rotated = y
    y_rotated = x

    return x_rotated, y_rotated

def calculate_pac_with_rotation(p_ab, p_bc, theta):
    """
    Menghitung posisi p_ac berdasarkan p_ab, p_bc, dan rotasi theta

    Args:
    p_ab (list): Vektor posisi dari titik a ke titik b [x, y, z]
    p_bc (list): Vektor posisi dari titik b ke titik c [x, y, z]
    theta (float): Sudut rotasi dalam radian

    Returns:
    list: Vektor posisi dari titik a ke titik c [x, y, z]
    """
    # Matriks rotasi 2D
    R_ab = np.array([
        [np.cos(theta), -np.sin(theta), 0],
        [np.sin(theta), np.cos(theta), 0],
        [0, 0, 1]
    ])
    
    # Matriks transformasi homogen
    T_ab = np.identity(4)
    T_ab[:3, :3] = R_ab
    T_ab[:3, 3] = p_ab
    
    # Vektor homogen p_bc
    p_bc_hom = np.append(p_bc, 1)
    
    # Menghitung p_ac
    p_ac_hom = T_ab @ p_bc_hom
    p_ac = p_ac_hom[:3]
    
    return p_ac

def eksekusi(robot_pose_msg, ball_pose_msg):
    # Mendapatkan posisi robot dari handle_robot_pose()
    robot_pos = handle_robot_pose(robot_pose_msg)
    xpos_robot, ypos_robot, theta_robot = robot_pos
    
    # Mendapatkan posisi bola dari handle_ball_pose()
    ball_pos = handle_ball_pose(ball_pose_msg)
    x_ball, y_ball = ball_pos
    
    # Menampilkan hasilnya
    print("Posisi robot (x, y, theta):", xpos_robot, ypos_robot, theta_robot)
    print("Posisi bola (x, y):", x_ball, y_ball)

def main():
    rospy.init_node('tf2_ball_broadcaster')
    # turtlename = rospy.get_param('~balls')
    rospy.Subscriber('ballPos_topic', Pose, handle_ball_pose)
    rospy.Subscriber('robot_pos', Pose, handle_robot_pose)
    rospy.spin()

if __name__ == '__main__':
    main()