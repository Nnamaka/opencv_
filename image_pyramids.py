# 4:50:00
import numpy as np
import cv2 as 🇨🇻 

# we can use pyramids to search for faces
# we have guassian pyramid and laplace pyramid.
# laplace pyramid helps us blend and reconstruct the pyramid

img = cv.imread('lena.jpg')
lr1 = cv.pyrDown(img)
lr2 = cv.pyrDown(lr1)

cv.imshow('original image',img)
cv.imshow('original image',img)
cv.imshow('original image',img)

cv.waitKey(0)
cv.destroyAllWindows()

# bending images with laplace
# 4:57:18