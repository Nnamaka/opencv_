
# morphological transformations are some simple operations based on
# the image shape. it is normally performed on a binary image.
# we need two things to perform morphological transformation:
# 1.The image 2. A Kernal
# a kernel tells you how to change the value of any given pixel
# by combining it with different amounts of the neighboring pixels
# morpholoagical method include; erosion, dialation, opening and 
# closing method

import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('lena.jpg', cv.IMREAD_GRAYSCALE)

# morphogical transformation-----
# 1.dilation removes dots/spots from image
# 2.erosion is another morphological transformation
# 3.opening operation
# 4.closing operation
# 5.morphological gradient
# 6.Tophat
# etc

# example of how to apply this operation
# => cv.morphologyEx(mask, cv.MORPH_OPEN, kernal)
# etc.

titles = ['images']
images = [img]

for i in range(1):
    plt.subplot(1, 1, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()