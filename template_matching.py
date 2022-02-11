
# 6:17:27

# Template matching is a method of searching and finding the location
# of a template image inside a larger image
# we use match templ  for achieving this
# we use this methods to find sections of an image, given the
# image template for searching. we can pass the image and
# the method, we can pass the 
# template searching function cv.matchTemplate()
# 1.TM_SQDIFF
# 2.TM_SQDIFF_NORMED
# 3.TM_CCORR_NORMED
# 4.TM_CCOEFF
# 5.TM_CCOEFF_NORMED

import numpy as np 
import cv2 as cv

img = cv.imread("messi.jpg")

cv.imshow('img', img)
cv.waitKey(0)
cv.destroyAllWindows()