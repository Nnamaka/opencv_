
# 6:01:31

# histogram in opencv
# a histogram is a graph or a plot that gives you an overall idea
# of the intensity distribution of an image

import numpy as np 
import cv2 as cv
from matplotlib import pyplot as plt

#img = np.zeros((200,200), np.uint8)
img = cv.imread('lena.jpg')

# split your image into BGR
#b, g, r = cv.split(img)

# ways to find the histogram of an image
# 1.Use matplot plt.hist()
# 2.Use opencv cv.calcHist()

#plt.hist(img.ravel(), 256, (0,256))
#plt.hist(b.ravel(), 256, [0,256])
#plt.hist(g.ravel(), 256, [0,256])
#plt.hist(r.ravel(), 256, [0,256])
#plt.show()

hist = cv.calcHist([img], [0], None, [256], [0,256])
plt.plot(hist)
plt.show()
#cv.imshow('img', img)

cv.waitKey(0)
cv.destroyAllWindows()