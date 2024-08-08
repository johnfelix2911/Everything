import cv2
import numpy as np


start=0
while True:
    if (start//360)%3==0:
        img=np.full((500,500,3),(0,0,0),dtype=np.uint8)
        cv2.ellipse(img,(250,250),(100,100),0,start,start+2,(255,255,255),18)
        start=start+5
    if (start//360)%3==1:
        cv2.ellipse(img,(250,250),(100,100),0,start,start+2,(255,255,255),18)
        start=start+5
    if (start//360)%3==2:
        cv2.ellipse(img,(250,250),(100,100),0,start,start+2,(0,0,0),18)
        start=start+5
    cv2.imshow("hehe",img)
    if cv2.waitKey(10)==ord("q"):
        break
cv2.destroyAllWindows()