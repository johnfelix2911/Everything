import cv2
img1=cv2.imread("img1.png",cv2.IMREAD_COLOR)
cv2.imshow("img1",img1)
cv2.waitKey(0)
img2=cv2.imread("img2.png",cv2.IMREAD_COLOR)
cv2.imshow("img1",img2)
cv2.waitKey(0)
#now subtract
