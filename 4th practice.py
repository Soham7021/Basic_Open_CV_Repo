#4th video lecture
import cv2
cap = cv2.VideoCapture(0)
while(True):

    ret, a = cap.read()
    cv2.imshow("abvc", a)
    cv2.waitKey(1)
  

cap.release()
cv2.destroyAllWindows()