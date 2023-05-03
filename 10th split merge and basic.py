import numpy as np
import cv2

img = cv2.imread("messi5.jpg")

print("no of rows coloumns and the channel :",img.shape)# it will return tuple of no. rows,columns, and the channeles
print("The pixels of image : ",img.size)#it will return the no. of pixels that are accesed in total
print("Data type of the image : ",img.dtype)# it will return the datatype of the image
b,g,r = cv2.split(img)# it will split your image in three channels
img = cv2.merge((b,g,r))

ball = img[280:340, 330:390]
img[273:333, 100:160] = ball
#we just copied the image from one place and pested to another
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
