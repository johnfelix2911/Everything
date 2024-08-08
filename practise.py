import cv2
import numpy as np
img=np.full((500,500,3),255,dtype=np.uint8)
img[200:300,200:300,:]=[0,0,0]
#img[200:300,300:200]=0
cv2.imshow("img",img)
cv2.waitKey(0)