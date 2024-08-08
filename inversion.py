import cv2
img1=cv2.imread('image.png')
dest_pic2=cv2.bitwise_not(img1,mask=None)
cv2.imshow('Orig',img1)
cv2.imshow('Bitwise NOT on image 1',dest_pic2)

# de-allocate any associated memory usage
if cv2.waitKey(0) & 0xff==27:
    cv2.destroyAllWindows()