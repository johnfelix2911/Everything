import cv2
import numpy as np

'''img=cv2.imread("pic2.jpg",1)
img_2=img[:,:,:10]
img2=np.zeros(())
cv2.imshow("img",img)
cv2.imshow("img2",img_2)'''

'''img=np.full((500,500,3),255,dtype=np.uint8)
img[200:300,200:300,:]=[0,0,0]
#img[200:300,300:200]=0
cv2.imshow("img",img)
cv2.waitKey(0)'''

'''img=np.full((500,500,3),0,dtype=np.uint8)
cv2.circle(img,(250,250),60,[0,0,255],4) #60 is radius and 4 is thickness
cv2.imshow("image",img)
cv2.waitKey(0)'''

img=np.full((500,500,3),0,dtype=np.uint8)
steps=5
h=200
w=200
flag=0
while True:
    if flag==0:
        cv2.rectangle(img,[w,h],[w+100,h+100],[0,255,0],-1)
        h+=steps
        #w+=steps
        cv2.rectangle(img,[w,h],[w+100,h+100],[0,0,255],10)
        cv2.imshow("img",img)
        cv2.waitKey(1)
        if (h+100)>=500:
            flag=1
    if flag==1:
        cv2.rectangle(img,[w,h],[w+100,h+100],[0,255,0],-1)
        h-=steps
        #w-=steps
        cv2.rectangle(img,[w,h],[w+100,h+100],[0,0,255],10)
        if h<=0:
            flag=0
    #cv2.imshow("hello",img)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
    cv2.imshow("img",img)
    cv2.waitKey(1)