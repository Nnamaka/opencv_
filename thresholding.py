
# 2:54:59

# thresholding is a technique used from seperating an object from
# its background. The process of thresholding involve comparing
# every pixel of an image with a predefined threshold value

import cv2 as cv
import numpy as np

img = cv.imread('lena.jpg', 0)

_, th1 = cv.threshold(img, 50, 255, cv.THRESH_BINARY)
_, th2 = cv.threshold(img, 50, 255, cv.THRESH_BINARY_INV)
_, th3 = cv.threshold(img, 50, 255, cv.THRESH_TRUNC)
_, th4 = cv.threshold(img, 50, 255, cv.THRESH_TOZERO)
_, th5 = cv.threshold(img, 50, 255, cv.THRESH_TOZERO_INV)

cv.imshow('image', img)

cv.imshow('th1', th1)
cv.imshow('th2', th2)
cv.imshow('th3', th3)
cv.imshow('th4', th4)
cv.imshow('th5', th5)

cv.waitKey(0)
cv.destroyAllWindows()

# adaptive thresholding is better