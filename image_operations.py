import numpy as np
import cv2 as cv


img = cv.imread('messi.jpg')

print(img.shape)
print(img.size)
print(img.dtype)

b, g, r = cv.split(img)
img = cv.merge( (b,g,r))

# ROI operations
ball = img[280:340, 330:390]
img[273:333, 100:160] = ball

#cv.imshow('image', img)
#cv.waitKey(0)
#cv.destroyAllWindows

# adding two images ( images must be of the same size)
#img2 = cv.imread('lena.jpg')
#img2 = cv.resize(img2, (512,512))

#img = cv.resize(img, (512,512))

#result = cv.add(img, img2)

# you can use cv.addWeighted() for emphasis on a particular image


cv.imshow('image', result )
cv.waitKey(0)
cv.destroyAllWindows