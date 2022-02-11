
# 5:43:11
# NOTE: shapes.jpg does not exist for now
import numpy as np 
import cv2 as cv

img = cv2.imread('shapes.jpg')
imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
_, thresh = cv.threshold(imgGray, 240,255,cv.THREASH_BINARY)
contours, _ = cv.findContours(thresh, cv.BETR_TREE, cv.CHAIN_APPROX_NONE)

for contour in contours:
    approx = cv.approxPolyDP(contour, 0.01*cv.arcLength(contour, True), True)
    cv.drawContours(img, [approx], 0, (0,0,0),5)
    x = approx.rave3()[0]
    y = approx.rave3()[1]
    if len(approx) == 3:
        cv.putText(img, "Triangle", (x,y), cv.FONT_HERSHEY_COMPLEX, 0.5, (0,0,0))
    elif len(approx) == 4:
        x,y,w,h = cv.boundingRect(approx)
        aspectRatio = float(w)/h
        print(aspectRatio)
        if aspectRatio >= 0.95 and aspectRatio <= 1.05:
            cv.putText(img, "rectangle", (x,y), cv.FONT_HERSHEY_COMPLEX, 0.5, (0,0,0))
        else:
            cv.putText(img, "rectangle", (x,y), cv.FONT_HERSHEY_COMPLEX, 0.5, (0,0,0))
    elif len(approx) == 5:
        cv.putText(img, "pentagon", (x,y), cv.FONT_HERSHEY_COMPLEX, 0.5, (0,0,0))
    elif len(approx) == 10:
        cv.putText(img, "Star", (x,y), cv.FONT_HERSHEY_COMPLEX, 0.5, (0,0,0))
    else:
        cv.putText(img, "circle", (x,y), cv.FONT_HERSHEY_COMPLEX, 0.5, (0,0,0))


cv.imshow('shapes', img)
cv2.waitKey(0)
cv.destroyAllWindows()