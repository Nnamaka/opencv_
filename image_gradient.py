
import cv2 as cv
import numpy as np 
from matplotlib import pyplot as plt

# image gradient is a direction change in the intensity or color
# in an image
# we can use image gradient to find edges inside an image
# the three types are:
# 1.laplace => cv.Laplacian()
# 2.sobel_X method => cv.Sobel()
# 3.sobel_Y method => cv.Sobel()

img = cv.imread('lena.jpg', cv.IMREAD_GRAYSCALE)

# applying the laplace method in and image
lap = cv.Laplacian(img, cv.CV_64F)
lap = np.uint8(np.absolute(lap))

titles = ['image','lap']
images = [img, lap]
for i in range(2):
    plt.subplot(1, 2, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()

