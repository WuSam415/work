import cv2

# video = cv2.VideoCapture(0)
faceCascade = cv2.CascadeClassifier("C:\\Python\\Python38\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml")

src_image = cv2.imread("manutd.jpg")
gray_image = cv2.cvtColor(src_image, cv2.COLOR_BGR2GRAY)

# Detect faces in the image

faces_rects = faceCascade.detectMultiScale(gray_image, scaleFactor = 1.1, minNeighbors = 2)
print(type(faces_rects))
print(faces_rects[0])
print(faces_rects[1])
(a,b,c,d) = faces_rects[0]
print(b)

for(x,y,w,h) in faces_rects:
    cv2.rectangle(src_image, (x, y), (x+w, y+h), (0,255,0), 2)

cv2.imshow("Face", src_image)

cv2.waitKey(0)