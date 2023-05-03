import cv2
from matplotlib import pyplot as plt

img = cv2.imread("messi5.jpg",-1)
cv2.imshow('Image', img)
# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) #this just gives the same image color after using matplotlib also

plt.imshow(img)#used to display using plt
plt.xticks([]),plt.yticks([])#by using this the y-axis and x-axis will not be displayec
plt.show()#used to display using plt

cv2.waitKey(0)
cv2.destroyAllWindows()