import cv2
import imutils

src_image = cv2.imread("shapes_and_colors.jpg")
gray_image = cv2.cvtColor(src_image, cv2.COLOR_BGR2GRAY)
blur_image = cv2.GaussianBlur(gray_image, (5,5), 0)
thres_image = cv2.threshold(blur_image, 60, 255, cv2.THRESH_BINARY)[1]

contours = cv2.findContours(thres_image.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours = imutils.grab_contours(contours)

for contour in contours:
    M = cv2.moments(contour)
    print(M["m00"])
    if M["m00"] == 0:
        continue
    cX = int(M["m10"] / M["m00"])
    cY = int(M["m01"] / M["m00"])
    cv2.drawContours(src_image, [contour], -1, (0,255,0), 2)
    cv2.circle(src_image, (cX, cY), 7, (255,255,255), -1)
    cv2.putText(src_image, "center", (cX-20, cY-20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 2)

cv2.imshow("Source", src_image)
cv2.waitKey(0)
cv2.destroyAllWindows()