
# 6:36:00

# Hough is a popular technique to detect any shape, if you can 
# represent that shape in a mathematical form. it can detect the shape
# even if it is broken or distorted a little bit
# you can use hough method for lane lines detection on the road

# lets create a lane detection system
# 7:13:00

import matplotlib.pylab as plt 
import numpy as np 
import cv2 as cv


# designing region of interest and detecting the lane lines






# draw road lane lines 



# detecting circles using hough circle transform
# 8:00:00



# face detection with opencv using cascade detection technique
# 8:08
# on opencv github page, you can find saved classifiers for 
# different purpose

# face detection inside a video
face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')

cap = cv.Videocapture('test.mp4')

while cap.isOpened():
    _, img = cap.read()

    gray = cv.cvtColor(img, cv2.COLOR_BRG2GRAY)
    faces = face_cascade.detectMultiScale(gray,1.1,4)

    for(x, y, w, h) in faces:
        cv.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 3)

        cv.imshow('img',img)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()