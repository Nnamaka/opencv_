
# 5:15:00

# contours can be explained as a curve joining all the points on
# the boundary which are having the same colour of intensity.
# they can be used for object detection, object classification

import numpy as np
import cv2 as cv

img = cv.imread('lena.jpg')
imgray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

cv.imshow('image', img)
cv.imshow('image GRAY', imgray)
cv.waitKey(0)
cv.destroyAllWindows()