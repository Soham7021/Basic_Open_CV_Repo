import numpy as np
import cv2

img = cv2.imread("messi5.jpg")
img2 = cv2.imread("ronaldo7.jpg")

img = cv2.resize(img, (512,512))
img2 = cv2.resize(img2, (512,512))


# mixx = cv2.add(img, img2)


# #if the size of the images will be different then it will give the error so first match the sizes of the images
#there is anothe method to assign the same task more specific

mixx = cv2.addWeighted(img, .6, img2, .4, 0 )

cv2.imshow('image', mixx)
cv2.waitKey(0)
cv2.destroyAllWindows()