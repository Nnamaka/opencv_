
# 2:53:55

# HSV (Hue, Saturation and value)
# Hue corresponds to the color components with a range from 0-360
# saturation is the amount of color(depth of the pigment)
# 0-100%
# value is basically the brightness of the color
# 0-100
# red, yellow, blue, green, cyan and magenta 

import cv2 as cv
import numpy as np

def nothing(x):
    pass

cv.namedWindow('Tracking')
#cv.createTrackbar('LH','Tracking', 0, 255, nothing)
#cv.createTrackbar('LS', 'Tracking',0,255,nothing)
#cv.createTrackbar('LV', 'Tracking',0,255,nothing)
#cv.createTrackbar('UH', 'Tracking',255,255,nothing)
#cv.createTrackbar('US', 'Tracking',255,255,nothing)
#cv.createTrackbar('UV', 'Tracking',255,255,nothing)

while (1):
    frame = cv.imread('lena.jpg')
    hsv = cv.cvtColor(frame,cv.COLOR_BGR2HSV)
    l_b = np.array([110,50,50])
    u_b = np.array([130,255,255])

    mask = cv.inRange(hsv, l_b,u_b)
    res = cv.bitwise_and(frame, frame, mask=mask)

    cv.imshow("frame", frame)
    cv.imshow('mask', mask)
    cv.imshow('res', res)

    key = cv.waitKey(1)
    if key == 27:
        break