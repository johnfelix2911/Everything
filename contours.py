import cv2
import numpy as np

img2=cv2.imread("shapes.jpg")
img=cv2.imread("shapes.jpg",0)

ret,img=cv2.threshold(img,127,255,cv2.THRESH_BINARY)
edged=cv2.Canny(img2,30,200)
contours,hierarchy=cv2.findContours(edged,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

cv2.imshow('canny edges after contouring',edged)
print("number of contours found="+str(len(contours)))
cv2.drawContours(img2,contours,-1,(0,255,0),3)

cv2.imshow('Contours',img2)
cv2.waitKey(0)
cv2.destroyAllWindows()