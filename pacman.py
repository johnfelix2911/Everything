import cv2
import numpy as np
flag=0
step=0
img=np.full((500,500,3),0,dtype=np.uint8)
cv2.ellipse(img,(250,250),(50,50),0,-135,135,(0,0,255),-1)
cv2.imshow("img",img)
cv2.waitKey(0)
while True:
    img=np.full((500,500,3),0,dtype=np.uint8)
    cv2.ellipse(img,(250,250),(50,50),0,-135-step,135+step,[0,0,255],-1)
    if flag==0:
        step+=1
    if step >=45:
        flag=1
    if step <=0:
        flag=0
    if flag==1:
        step-=1

    cv2.imshow("img",img)
    cv2.waitKey(1)