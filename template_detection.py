import cv2
import numpy as np
img=cv2.imread("image.jpg")
img2=cv2.imread("template.jpg")


#cv2.rectangle(img,(50,50),(100,100),10)

img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img2_gray=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

h,w=img2.shape[0:2]
print(h, w)

result=cv2.matchTemplate(img,img2,cv2.TM_CCOEFF_NORMED)

min_val,max_val,min_loc,max_loc=cv2.minMaxLoc(result)

threshold=0.6
loc=np.where(result>=threshold)
print(loc)

for pt in zip(*loc[::-1]):
    #print(pt)
    cv2.rectangle(img,(pt[0],pt[1]),(pt[0]+w,pt[1]+h),(0,0,255),2)

cv2.imshow("image",img)
cv2.imshow("imag33e",result)
cv2.waitKey(0)
cv2.destroyAllWindows()



#cv2.rectangle(img_gray,(min_loc[0],min_loc[1]),(min_loc[0]+h,min_loc[1]+w),255,25)
'''cv2.rectangle(img_gray,(min_loc[0],min_loc[1]),(min_loc[0]+w,min_loc[1]+h),255,2)

#cv2.imshow('iop', result)
cv2.imshow("img",img_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()'''