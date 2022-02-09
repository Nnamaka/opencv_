
# 2:29:19
import cv2 as cv
import numpy as np

def nothing(x):
    print(x)

img = np.zeros((300,512,3), np.uint8)
cv.namedWindow('image')

# to create a trackbar
cv.createTrackbar('B','image',0 , 255, nothing)
cv.createTrackbar('G','image',0 , 255, nothing)
cv.createTrackbar('R','image',0 , 255, nothing)

# how to add a swithc using a trackbar
while(1):
    cv.imshow('image',img)
    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break
    # how to change the values in your image
    b = cv.getTrackbarPos('B', 'image')
    g = cv.getTrackbarPos('G', 'image')
    r = cv.getTrackbarPos('R', 'image')

    img[:] = [b, g, r]


cv.destroyAllWindows()