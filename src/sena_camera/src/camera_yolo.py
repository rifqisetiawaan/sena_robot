#!/usr/bin/env python3

# cam stream program, pub ke yolo_dist
import rospy
import numpy as np
from geometry_msgs.msg import Pose
from open_base.msg import Movement
import math
import cv2
from prcs_image.msg import squareInfo
from prcs_image.image_process import process_img as pr
from prcs_image.command_vel import velo as vl
from ultralytics import YOLO


message = Pose()

def get_center_coordinates(box):
    x_min, y_min, x_max, y_max = box
    x_center = (x_min + x_max) / 2
    y_center = (y_min + y_max) / 2
    return x_center, y_center

def angle_between_points(anchor, point1, point2):
    # anchor, point1, point2 are tuples (x, y)
    
    # Vector AB
    vector_AB = (point1[0] - anchor[0], point1[1] - anchor[1])
    
    # Vector AC
    vector_AC = (point2[0] - anchor[0], point2[1] - anchor[1])
    
    # Calculate angles using arctangent (atan2) and convert to degrees
    angle_AB = math.degrees(math.atan2(vector_AB[1], vector_AB[0]))
    angle_AC = math.degrees(math.atan2(vector_AC[1], vector_AC[0]))
    
    # Calculate the angle between AC and AB
    angle_between = angle_AC - angle_AB
    
    # Adjust the angle to be within 0 to 360 degrees
    if angle_between < 0:
        angle_between += 360
    return angle_between

# radius (distance) calculation in pixel
def radius_calc(x, y):
    radius = math.sqrt((x-325)**2 + (y-240)**2)
    return radius

def regresi(px_dist):
    real_dist = 10**(0.0091 * px_dist + 0.679)
    return real_dist

# image to real world coordinate
def px_real_conversion(dist_real, theta):
    xreal = dist_real * math.cos(theta)
    yreal = dist_real * math.sin(theta)
    return xreal, yreal

def publish_message():
    Ballpub = rospy.Publisher('ballPos_topic', Pose, queue_size=10)
    Obspub = rospy.Publisher('obsPos_topic', Pose, queue_size=10)
    rospy.init_node('camera_yolo', anonymous=False)
    
    rate = rospy.Rate(10)

    cap = cv2.VideoCapture(0)
    fps = cap.get(cv2.CAP_PROP_FPS)
    model = YOLO('/home/krsbi/sena_robot/src/sena_camera/yolo/best.pt')
    poseBall = Pose()
    poseObs = Pose()
    while not rospy.is_shutdown():
        # capture frame by frame
        ret, frame = cap.read()
        # frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
        poseBall.position.x = 0.0
        poseBall.position.y = 0.0
        poseObs.position.x = 0.0
        poseObs.position.y = 0.0

        if ret==True:            
            results = model(frame, conf=0.6)
            frame = results[0].plot()
            # Extract bounding boxes, classes, names, and confidences
            boxes = results[0].boxes.xyxy.tolist()
            classes = results[0].boxes.cls.tolist()
            names = results[0].names
            confidences = max([results[0].boxes.conf.tolist()])
            # plot titik tengah kamera
            cv2.circle(frame, (325, 240),
                    radius=30, color=(0, 0, 255), thickness=1)
            # cv2.circle(frame, (340, 240), 
            #         radius=30, color=(0, 0, 255), thickness=1)

            # Iterate through the results
            for box, cls, conf in zip(boxes, classes, confidences):
                x1, y1, x2, y2 = box
                confidence = conf
                detected_class = cls
                name = names[int(cls)]
                # print("----START----")
                # print("BOX----")
                # print(box)
                # print("CLS----")
                # print(cls)
                # print("CONF---")
                # print(conf)
                # print("----END----")

                if classes == [1.0, 0.0]:
                    # hitung centroid bola
                    x1b, y1b, x2b, y2b = boxes[1]
                    cent_bola = pr.process_image.find_centroid(x1b, y1b, x2b, y2b)
                    
                    # hitung centroid kotak
                    x1k, y1k, x2k, y2k = boxes[0]
                    cent_kotak = pr.process_image.find_centroid(x1k, y1k, x2k, y2k)
                    # plot hasil centroid
                    pr.process_image.plot_line(frame, cent_bola)
                    pr.process_image.plot_line(frame, cent_kotak)
                    print(str(cent_bola)+str(cent_kotak))
                    cbx, cby = cent_bola
                    ckx, cky = cent_kotak
                    # lempar ke message Point32 hasil centroid
                    poseBall.position.x = cbx
                    poseBall.position.y = cby
                    poseObs.position.x = ckx
                    poseObs.position.y = cky
                elif classes == [0.0, 1.0]:
                    # hitung centroid bola
                    x1b, y1b, x2b, y2b = boxes[0]
                    cent_bola = pr.process_image.find_centroid(x1b, y1b, x2b, y2b)
                    # hitung centroid kotak
                    x1k, y1k, x2k, y2k = boxes[1]
                    cent_kotak = pr.process_image.find_centroid(x1k, y1k, x2k, y2k)
                    # plot hasil centroid
                    pr.process_image.plot_line(frame, cent_bola)
                    pr.process_image.plot_line(frame, cent_kotak)
                    print(str(cent_bola)+str(cent_kotak))
                    cbx, cby = cent_bola
                    ckx, cky = cent_kotak
                    # lempar ke message Point32 hasil centroid bola
                    poseBall.position.x = cbx
                    poseBall.position.y = cby
                    poseObs.position.x = ckx
                    poseObs.position.y = cky

                elif classes == [0.0]:
                    # hitung centroid bola
                    x1b, y1b, x2b, y2b = boxes[0]
                    cbx, cby = get_center_coordinates(boxes[0])
                    # cby = cby - 240
                    # cbx = cbx + 325
                    # cbx = (640-(cbx-0))
                    # cby = (480-(cby-0))
                    theta = angle_between_points((325, 240), (325, 200), (cbx, cby))
                    radius = int(radius_calc(cbx, cby))
                    real_dist = regresi(radius)
                    xreal = real_dist * math.sin(math.radians(theta))
                    yreal = real_dist * math.cos(math.radians(theta))
                    poseBall.position.x = xreal
                    poseBall.position.y = yreal
                    poseBall.orientation.x = 0
                    poseBall.orientation.y = 0
                    poseBall.orientation.z = 0.71
                    poseBall.orientation.w = 0.71
                    poseObs.position.x = 0.0
                    poseObs.position.y = 0.0
                    font = cv2.FONT_HERSHEY_SIMPLEX
                    cbx = int(cbx)
                    cby = int(cby)
                    cv2.circle(frame, (325, 240), radius=0, color=(255, 255, 255), thickness=3)
                    cv2.circle(frame, (325, 240), radius=radius, color=(0, 255, 255), thickness=3)
                    cv2.circle(frame, (cbx, cby), radius=0, color=(0, 255, 255), thickness=3)
                    cv2.line(frame, (325, 240), (cbx, cby),
                             color=(0, 0, 255), thickness=1)
                    cv2.line(frame, (325, 240), (325, 200),
                             color=(0, 0, 255), thickness=1)
                    
                    cv2.putText(frame,'KIROSENA INTERFACE', 
                                (50, 50), font, 0.5,
                                (0, 255, 255), 1, cv2.LINE_4)
                    cv2.putText(frame,'Angle Bola: '+str("%.2f" % theta)+' deg', 
                                (50, 65), font, 0.5,
                                (0, 255, 255), 1, cv2.LINE_4)
                    cv2.putText(frame,'Distance Bola px: '+str("%.2f" % radius)+' px', 
                                (50, 80), font, 0.5,
                                (0, 255, 255), 1, cv2.LINE_4)
                    cv2.putText(frame,'Distance Bola: '+str("%.2f" % real_dist)+' cm', 
                                (50, 95), font, 0.5,
                                (0, 255, 255), 1, cv2.LINE_4)
                    cv2.putText(frame,'Pixel X: '+str("%.2f" % cbx)+' px', 
                                (50, 110), font, 0.5,
                                (0, 255, 255), 1, cv2.LINE_4)
                    cv2.putText(frame,'Pixel Y: '+str("%.2f" % cby)+' px', 
                                (50, 125), font, 0.5,
                                (0, 255, 255), 1, cv2.LINE_4)
                    cv2.putText(frame,'Real X: '+str("%.2f" % xreal)+' cm', 
                                (50, 140), font, 0.5,
                                (0, 255, 255), 1, cv2.LINE_4)
                    cv2.putText(frame,'Real Y: '+str("%.2f" % yreal)+' cm', 
                                (50, 155), font, 0.5,
                                (0, 255, 255), 1, cv2.LINE_4)
                    cv2.putText(frame,'FPS: '+str(fps), 
                                (50, 170), font, 0.5,
                                (0, 255, 255), 1, cv2.LINE_4)

                else:
                    poseBall.position.x = 0.0
                    poseBall.position.y = 0.0
                    poseObs.position.x = 0.0
                    poseObs.position.y = 0.0


            # Display the annotated frame
            cv2.imshow("YOLOv8 Inference", frame)
            # Break the loop if 'q' is pressed
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
            # publish message
            Ballpub.publish(poseBall)
            Obspub.publish(poseObs)

        rate.sleep()
        

if __name__ == '__main__':
    try:
        publish_message()
    except rospy.ROSInterruptException:
        pass

# run sebelum dibuat roslaunch:
# rosrun camera_yolo camera_yolo.py
# rosrun rosserial_arduino serial_node.py _port:=/dev/ttyUSB1
# rostopic echo /video_topic