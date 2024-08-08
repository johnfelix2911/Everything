import cv2
import numpy as np
vid=cv2.VideoCapture(0)
while True:
    _,img=vid.read()
    temp=cv2.imread("name.jpg")
    

    cv2.imshow("hehe",img)
    k=cv2.waitKey(1)
    if k==ord("q"):
        break
cv2.destroyAllWindows()