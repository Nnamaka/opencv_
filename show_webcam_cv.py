
import cv2

#img = cv2.imread("lena.jpg",-1)

#cv2.imshow('smy',img)
#cv2.waitKey(0)
#cv2.destroyAllwindows()

# 0 is first camera, 1 is second camera , 3 is third

cap = cv2.VideoCapture(0)
# display video from video file
# cap = cv2.VideoCapture("name.mp4")

while True:
    ret, frame = cap.read()

    # get width and height of frame(video/image) 
    #cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    #cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

    # convert color output to grey
    #grey = cv2.cvtoColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow('webcam', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()