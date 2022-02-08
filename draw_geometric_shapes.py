
import cv2 as cv
import numpy as np

img = cv.imread('lena.jpg', 1)
#creat image from numpy zeros
# img = np.zeros([512,512,3], np.uint8 )

# lets draw a line on the image

# the fourth argument chooses the color in RGB format
# but our image is loaded in BGR format. so we can pick an
# rgb color code from google search by typing "rgb color picker",
# when we get the channels say; 44,96, 144 , we input it in the 
# function argument in the reverse order

# the second argument is the coordinates, and by default the 
# shapes are drawn in the top left coordinates
img = cv.line(img,(0,0),(255,255), (255,0,0), 5)

# to draw rectangel, arrowedline ,circle, we can use there respective
# functions cv2.rectangel(), cv2.arrowedLine(), cv2.circle()

# to puttext, we use a methon called put text
# font = cv2.FONT_HERSHEY_SIMPLEX
# img = cv2.putText(img, 'the text', font,...)

cv.imshow('image',img)

cv.waitKey(0)
cv.destroyAllWindows()