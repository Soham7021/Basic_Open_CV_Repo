# 4ht video lecture

import cv2

cap = cv2.VideoCapture(0);#0 and -1 are the default values for this


#we can open the video files from the device jut put file neame instead of that 0 in the inverted commas

while(True):
    #we can use cap.isOpened for the true value insted of directly using true;
    #its like if that video is opend then it is true
    ret, frame = cap.read()
    
    print("The Height is :",cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    print("The width is : ",cap.get(cv2.CAP_PROP_FRAME_WIDTH))

    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #this is how we can change the color of the video 


    cv2.imshow('frame', frame)# just replace "frame" with "grey" to get the video in balck and white


   #True is saved in the "ret" and the picture will be go in the "Frame" Variabel
    
    if cv2.waitKey(1) & 0xFF == ord("e"):
        break
    # for images we use '0' and for videos we use '1' for waitkey to display it infinitly

    #0xFF is inbuilt if you want to press any kay without defining it refer 2nd assighnment
    
    #as soon as we press "e" frame will be exited

cap.release()
cv2.destroyAllWindows()
print("The Height is :",cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print("The width is : ",cap.get(cv2.CAP_PROP_FRAME_WIDTH))