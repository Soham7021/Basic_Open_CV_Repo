import cv2
import numpy as np


img1 = np.zeros((324,324,3),np.uint8)
img1 = cv2.rectangle(img1,(200,0),(300,100),(255,255,255),-1)
img2 = cv2.imread('blackwhite.jpg')

# bitAnd = cv2.bitwise_and(img2, img1)


#thus when we will see the output of this we will know that by comparing img1 and img2 that black act as false and white act as true so by applying boolen knowledge we will get the third image on the basis of that
#similarly we can do it for the OR, NOT and XOR


#bitOR = cv2.bitwise_or(img2, img1)
#bitNOT = cv2.bitwise_not(img2)
bitXOR = cv2.bitwise_xor(img2, img1)

cv2.imshow("img1",img1)
cv2.imshow("img2",img2)
# cv2.imshow("bitAnd",bitAnd)
# cv2.imshow('bitOr', bitOR)
cv2.imshow('bitXOR', bitXOR)


cv2.waitKey(0)
cv2.destroyAllWindows()