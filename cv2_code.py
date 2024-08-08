import cv2
image=cv2.imread("image.png",cv2.IMREAD_COLOR)
cv2.imshow("image",image)
cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2
import numpy as np
import matplotlib.pyplot as plt

half=cv2.resize(image,(0,0),fx=0.1,fy=0.1)
bigger=cv2.resize(image,(1050,1610))

stretch_near=cv2.resize(image,(780,540),interpolation=cv2.INTER_LINEAR)

Titles=["Original","Half","Bigger","Interpolation Nearest"]
images=[image,half,bigger,stretch_near]
count=4

for i in range(count):  
    plt.subplot(2,2,i+1)
    plt.title(Titles[i])
    plt.imshow(images[i])

center_coordinates=(120,50)
radius=20
thickness=2
color=(255,0,0)
image=cv2.circle(image,center_coordinates,radius,color,thickness)

plt.show()

import cv2
image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow('image',image)
k=cv2.waitKey(0) & 0xFF
if k ==27:
    cv2.destroyAllWindows()

