
import cv2 as cv
import numpy as np

# bitwise operations are usefull when working
# with mask.
# masks are binary images that indicate the pixels in which
# an operation is to be performed
# 

img1 = np.zeros((250, 500, 3), np.uint8)
img1 = cv.rectangle(img1, (200, 0), (300, 100), (255,255,255),-1)
img2 = cv.imread('lena.jpg')

bitAnd = cv.bitwise_and

cv.imshow('img1', img1)
cv.imshow('img2', img2)

cv.waitKey(0)
cv.destroyAllWindows()
