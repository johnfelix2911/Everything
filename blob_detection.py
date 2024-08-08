import numpy as np
import cv2 as cv

image=cv.imread("bubbles.png",0)

param=cv.SimpleBlobDetector_Params()

param.minThreshold = 10
param.maxThreshold = 100
param.minArea = 200
param.filterByArea = True

detector = cv.SimpleBlobDetector_create(param)

keypoints = detector.detect(image)

image_with_keypoint=cv.drawKeypoints(image,keypoints,np.array([]),(0,0,255),cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv.imshow("image",image_with_keypoint)
cv.waitKey(0)
cv.destroyAllWindows()