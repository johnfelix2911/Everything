# Importing the modules 
import cv2 
import numpy as np 

# Reading the image 
image = cv2.imread('image.jpg') 

# Applying the filter 
medianBlur = cv2.medianBlur(image, 9) 

# Showing the image 
cv2.imshow('Original', image) 
cv2.imshow('Median blur', medianBlur) 

cv2.waitKey(0) 
cv2.destroyAllWindows() 
