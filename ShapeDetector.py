import cv2

class shapeDetector:
    def __init__(self):
        pass

    def detect(self, contour):
        shapeName = "Undefined"
        peri = cv2.arcLength(contour, True)
        # Common values for the second parameter to cv2.approxPolyDP 
        # are normally in the range of 1-5% of the original contour perimeter.
        approx = cv2.approxPolyDP(contour, 0.04 * peri, True)
        if(len(approx) == 3) :
            shape = "Triangle"
        elif(len(approx) == 4):
            # compute the bounding box of the contour and use the
			# bounding box to compute the aspect ratio
            (x,y,w,h) = cv2.boundingRect(approx)
            ar = w / float(h)
            # a square will have an aspect ratio that is approximately
			# equal to one, otherwise, the shape is a rectangle
            if ar >= 0.95 and ar <= 1.05:
                shape = "Square" 
            else: 
                shape = "Rectangle"
        elif(len(approx) == 5) : 
            shape = "Pentagon"
        else :
            shape = "Circle"
        return shape

