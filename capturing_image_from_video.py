
import cv2 as cv

#how to capture image from video
# we call the fourcc code class: look-up fourcc documentation
# then we call videowriter class
cap = cv.VideoCapture(0)
fourcc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter('output.avi', fourcc, 20.0, (640,480 ) )

while (cap.isOpened()):
    _, frame = cap.read()

    if _ == True:
        cap.get(cv.CAP_PROP_FRAME_WIDTH)
        cap.get(cv.CAP_PROP_FRAME_HEIGHT)

        out.write(frame)
        #cv.imshow('webcam', frame)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv.destroyAllWindows()

# set some properties to our video with
# cap.set()
# properties have numbers eg cv.CAP_PROP_FRAME_WIDTH number is 3
# cv.CAP_PROP_FRAME_HEIGHT is 4 

# change resolution of display
# cap.set(3, 1280)
# cap.set(4, 720)

