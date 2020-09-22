from ShapeDetector import shapeDetector
import argparse
import cv2
import imutils

image = cv2.imread("shapes_and_colors.jpg")
resized_image = imutils.resize(image, width = 300)
ratio = image.shape[0] / float(resized_image.shape[0])
gray_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)
blurred_image = cv2.GaussianBlur(gray_image, (5,5), 0)
# cv2.namedWindow("blurr")
# cv2.imshow("blurr", blurred_image)
thresh_image = cv2.threshold(blurred_image, 60, 255, cv2.THRESH_BINARY)[1]
# cv2.namedWindow("thresh_image")
# cv2.imshow("thresh_image", thresh_image)
contours = cv2.findContours(thresh_image.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours = imutils.grab_contours(contours)
print(len(contours))
myShapeDector = shapeDetector()

for contour in contours:
    M = cv2.moments(contour)
    cX = int((M["m10"] / M["m00"]) * ratio)
    cY = int((M["m01"] / M["m00"]) * ratio)
    shape = myShapeDector.detect(contour)
    contour = contour.astype("float")
    contour *= ratio
    contour = contour.astype("int")
    cv2.drawContours(image, [contour], -1, (0,255,0), 2)
    cv2.putText(image, shape, (cX, cY), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 2)
    cv2.imshow("Image", image)

cv2.waitKey(0)
cv2.destroyAllWindows()

