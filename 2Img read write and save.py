import cv2

img = cv2.imread("messi5.jpg ", 1)
print(img)
cv2.imshow("Image", img)
"""saving image if we press s and closing window if we press escape"""
a = cv2.waitKey(5000) 
if a == 27:
    cv2.destroyAllWindows()

elif a == ord("s"):#ord is inbuilt function to take character as input
    cv2.imwrite("Messi_copy.jpg", img)
    cv2.destroyAllWindows()