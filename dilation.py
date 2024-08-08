import cv2
import numpy as np

img = cv2.imread("map_final.jpg", 0)
kernel = np.array([[1,2,1],[2,10,2],[1,2,1]])
dilated_img = cv2.dilate(img, kernel, iterations=1)

cv2.imshow("Original", img)
cv2.imshow("Dilated", dilated_img)
cv2.waitKey(0)
cv2.destroyAllWindows()