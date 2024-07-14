#!/usr/bin/env python3

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import rospy
from geometry_msgs.msg import Pose, PoseStamped
import seaborn as sns
import signal
import sys

# Initialize global variables for position
x_data, y_data = [], []
x_bola, y_bola = [], []

# Callback function to update position data
def pose_callback(data):
    global x_data, y_data
    x_data.append(data.position.x)
    y_data.append(-data.position.y)  # Invert y data

# Callback function to update ball position data
def ball_callback(data):
    global x_bola, y_bola
    if not (data.pose.position.x == 0 and data.pose.position.y == 0):
        x_bola.append(data.pose.position.x)
        y_bola.append(-data.pose.position.y)

# Function to save the plot
def save_plot():
    fig.savefig("/home/krsbi/Pictures/robot_position_simulation.jpg")
    print("Plot saved successfully as JPG.")

# Signal handler for ROS shutdown
def signal_handler(sig, frame):
    print('ROS shutdown detected. Saving plot...')
    save_plot()
    sys.exit(0)

# Register the signal handler
signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)

# Initialize the ROS node
rospy.init_node('real_time_plotter')

# Subscriber to the robot_pos and ball_pos topics
rospy.Subscriber('robot_pos', Pose, pose_callback)
rospy.Subscriber('/move_base_simple/goal', PoseStamped, ball_callback)

# Set the Seaborn style
sns.set(style="darkgrid")

# Create a figure and axis for the plot
fig, ax = plt.subplots()
line, = ax.plot([], [], 'b-', marker='o', markersize=2)  # Line for robot movement
current_pos, = ax.plot([], [], 'ro', markersize=20)  # Red marker for current robot position
ball_line, = ax.plot([], [], 'g-', marker='o', markersize=2)  # Line for ball movement
ball_pos, = ax.plot([], [], 'go', markersize=20)  # Green marker for current ball position

# Initialize plot limits
def init():
    ax.set_xlim(-1, 3)  # Set these to the expected range of your data
    ax.set_ylim(-1, 3)
    ax.set_title('Robot Position Simulation')
    ax.set_xlabel('Y Position (meters)')  # Swapped
    ax.set_ylabel('X Position (meters)')  # Swapped
    return line, current_pos, ball_line, ball_pos

# Update the plot
def update(frame):
    line.set_data(y_data, x_data)  # Swapped
    ball_line.set_data(y_bola, x_bola)  # Swapped
    if y_data and x_data:  # Check if lists are not empty
        current_pos.set_data([y_data[-1]], [x_data[-1]])  # Update current position marker, swapped
    if y_bola and x_bola:  # Check if lists are not empty
        ball_pos.set_data([y_bola[-1]], [x_bola[-1]])  # Update ball position marker
    return line, current_pos, ball_line, ball_pos

# Create an animation with a faster update interval
ani = FuncAnimation(fig, update, init_func=init, interval=100, repeat=False)

# Show the plot
plt.show()

# Keep the script running
rospy.spin()
