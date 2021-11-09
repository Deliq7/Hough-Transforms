import cv2
import numpy as np

img = cv2.imread("h_line.png")

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
canny = cv2.Canny(gray,75,150)

lines = cv2.HoughLinesP(canny,1,np.pi/180,50,maxLineGap= 200) # 4 adet değişken tutuyor. (Doğruların başlangıç ve bitiş noktaları.)

for line in lines:
    x1,y1,x2,y2 = line[0]
    cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)


cv2.imshow("Gray",gray)
cv2.imshow("Hough Line Transform",img)

cv2.waitKey(0)
cv2.destroyAllWindows()

