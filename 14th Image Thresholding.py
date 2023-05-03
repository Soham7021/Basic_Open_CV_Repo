import cv2
import numpy as np

img = cv2.imread('colorgradint.jfif',0)
#in the above image black side is closer to 0 and right hand side is closer to 255
_, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)#(source,threshold vlaue,maxthreshold,threshold type)
_,th2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
#this is the exact inverse type of the  th1 all we are doing here is playing with the *TYPE* of the Threshold-

_,th3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
#we can observe in this type that after 127 the color is constant ,observe closely, this means the image will remain same untill 127*


_,th4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
#in this until 127 ,0 will be assined and further 127 i.e to the right the image will remain the same

_,th5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)# this is the exact opposite of the th4
cv2.imshow('Image', img)
cv2.imshow('th1', th1)
cv2.imshow('th2', th2)
cv2.imshow('th3', th3)
cv2.imshow('th4', th4)
cv2.imshow('th5', th5)

cv2.waitKey(0)
cv2.destroyAllWindows()