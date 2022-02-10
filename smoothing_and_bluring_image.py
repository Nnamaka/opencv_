
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
# the most common use of smoothing operation in an image is to
# remove noise in an image.
# when blurring or smoothing images, you can use diveres or linear
# filter
# example of other filters are
# Homogeneous filter, Gaussian filter, Median filter, Bilateral
# filter etc.

img = cv.imread('lena.jpg')

# convert image from BGR to RGB. matplot reads RGB format
# opencv reads the image in the BGR format
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

kernel = np.ones((5,5), np.float32)/25
dst = cv.filter2D(img, -1, kernel)

titles = ['image', '2D Convolution']
images = [img, dst]

# in homogeneous filter, each output pixel is the mean of its 
# kernal neighbors

# A kernel(convolution matrix or mask) is a small matrix.
# it is used for blurring, sharpening, embossing, edge detection
# and more. it is a shape which we can apply or convole over an
# image


for i in range(2):
    plt.subplot(1,2,i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()

# for one-dimensional signals images also can be filtered with
# various low-pass filters(LPF), high-pass filters(HPF) etc
# LPF is for removing noise, blurring the image
# HPF is for finding edges in the images

# median filter is good for fixing the salt-and-pepper noise
# bilateral filter is used to preserve the edges of the image