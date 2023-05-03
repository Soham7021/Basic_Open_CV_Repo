import cv2
"""Reading Image"""
img = cv2.imread("messi5.jpg ", 1)
#  1 :- Loads colored image
# 0 :- Loads image in greyscale
# -1 :- Loads image as such alpha channel 
print(img)


""" displaying IMage"""

cv2.imshow("Image", img)
cv2.waitKey(5000) # if we put 0 insted of 5000 image will never disapper
cv2.destroyAllWindows()


"""Writing an image in the form of file"""
cv2.imwrite("Messi_copy.jpg", img)#new image is created by messis copy name
