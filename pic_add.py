import cv2
image=cv2.imread("image.png",cv2.IMREAD_COLOR)
cv2.imshow("image",image)
cv2.waitKey(0)
cv2.destroyAllWindows()
image2=cv2.imread("image2.png",cv2.IMREAD_COLOR)
cv2.imshow("image2",image2)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.add(image,image2)
cv2.addWeighted(image,wt1,image2,wt2,0)