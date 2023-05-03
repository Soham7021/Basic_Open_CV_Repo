import cv2
import numpy as np

img = cv2.imread('sudokuu.jpg',0)

_, th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
#thus we can see the basic threshold is not working properly here due to uneven shade's we will be using adaptive threshold

th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
#now we can see it more clear color distribution
#the are two types of adaptive threshold 
#1st : ADAPTIVE_THRESH_MEAN_C
#2nd : ADAPTIVE_THRESH_GAUSIAN_C
th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
cv2.imshow('Image', img)
cv2.imshow('th1', th1)
cv2.imshow('th2', th2)
cv2.imshow('th3', th3)

cv2.waitKey(0)
cv2.destroyAllWindows()