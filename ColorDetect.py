import cv2
import numpy as np

# src_image = cv2.imread("circles.png")
src_image = cv2.imread("wire.jpeg")
cv2.namedWindow('src_image', cv2.WINDOW_NORMAL)
cv2.imshow('src_image', src_image)

hsv_image = cv2.cvtColor(src_image, cv2.COLOR_BGR2HSV)
cv2.namedWindow('hsv_image', cv2.WINDOW_NORMAL)
cv2.imshow('hsv_image', hsv_image)

# For blue
# lower_red = np.array([110,50,50])
# upper_red = np.array([130,255,255])

# For red
lower_red = np.array([169,100,100])
upper_red = np.array([189,255,255])

mask = cv2.inRange(hsv_image, lower_red, upper_red)
# mask = cv2.inRange(src_image, lower_red, upper_red)

cv2.namedWindow('mask', cv2.WINDOW_NORMAL)
cv2.imshow('mask', mask)

cv2.waitKey(0)
cv2.destroyAllWindows() 