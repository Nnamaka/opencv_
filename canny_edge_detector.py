
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
# the canny edge detector is an edge detection operator that uses
# a multi-stage algorithm to detect a wide range of edges in images.

# steps in canny edge detection
#1.Noise reduction
#2.Gradient calculation
#3.Non-maximum suppression
#4.Double threshold
#5.Edge Tracking by Hysteresis

img = cv.imread('lena.jpg',0)
canny = cv.Canny(img,100,200)

images = [img , canny]
title = ['image','canny']

for i in range(2):
    plt.subplot(1,1,i+1), plt.imshow(images[i], 'gray')
    plt.title(title[i])
    plt.xticks([]), plt.yticks([])

plt.show()