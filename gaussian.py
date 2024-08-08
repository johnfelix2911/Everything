# Importing the OpenCV, Numpy and Matplotlib libraries 
import cv2 
import numpy as np 
import matplotlib.pyplot as plt 

# Reading the image from the disk using cv2.imread() function 
# Showing the original image using matplotlib library function plt.imshow() 
img = cv2.imread('image.jpg') 
cv2.imshow('image', img) 

# Applying Gaussian Blur Filter using cv2.GaussianBlur() function 
# src is the source of image(here, img) 
# ksize is the size of kernel in the form A x B (here 3 x 3) 
# sigmaX is standard deviation of X axis 
# sigmaY is the standard deviation of Y axis 
# Since sigmaX and sigmaY is 0, the standard deviation the size of kernel 
gaussian_blur = cv2.GaussianBlur(src=img, ksize=(3,3),sigmaX=0) 

# Showing the Gaussian blur image using matplotlib library function plt.imshow() 
cv2.imshow('gaussian', gaussian_blur) 
cv2.waitKey(0)
cv2.destroyAllWindows()
