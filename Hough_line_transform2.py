import cv2
import numpy as np

cap = cv2.VideoCapture("line.mp4")

while True:
    _,frame = cap.read()
    frame = cv2.resize(frame,(640,480))
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lower_y= np.array([18, 94, 140],np.uint8)
    upper_y = np.array([48, 255, 255], np.uint8)
    mask = cv2.inRange(hsv,lower_y,upper_y)

    lines = cv2.HoughLinesP(mask,1,np.pi/180,50,maxLineGap= 250)

    for line in lines:
        x1,y1,x2,y2 = line[0]
        cv2.line(frame,(x1,y1,),(x2,y2),(0,0,255),2)


    cv2.imshow("Hough Line Transform",frame)
    if cv2.waitKey(20) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()