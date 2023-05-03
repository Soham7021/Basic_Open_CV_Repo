# 4ht video lecture

import cv2

cap = cv2.VideoCapture(0);
fourcc = cv2.VideoWriter_fourcc(*'XVID')
save = cv2.VideoWriter('MY_VIDEO.avi',fourcc,20.0, (640,480))

#where 20 is no. of frames per second we want 
 #640 and 480 is height and widht
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:

        cv2.imshow('frame', frame)
        save.write(frame)
    
        if cv2.waitKey(1) & 0xFF == ord("e"):
            break
    else:
        break


cap.release()
save.release()
cv2.destroyAllWindows()
