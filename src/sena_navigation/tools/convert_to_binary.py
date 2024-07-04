#!/usr/bin/env python3
import cv2 # Import OpenCV
   
# read the image file
img = cv2.imread('/home/krsbi/sena2024_ws/src/maps/lapangan_v3/lapangan _2632.png', cv2.IMREAD_GRAYSCALE)
   
ret, bw_img = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY|cv2.THRESH_OTSU)
   
# converting to its binary form
bw = cv2.threshold(img, 240, 255, cv2.THRESH_BINARY)
  
# Display and save image 
cv2.imshow("Binary", bw_img)
cv2.imwrite("/home/krsbi/sena2024_ws/src/maps/lapangan_v3/lapangan_binary_2632.png", bw_img)
cv2.waitKey(0)
cv2.destroyAllWindows()