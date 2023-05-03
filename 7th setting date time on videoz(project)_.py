import cv2
import datetime

cap = cv2.VideoCapture(0)
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))

# cap.set(4, 720)
# cap.set(3, 1280)

# print(cap.get(4))
# print(cap.get(3))


while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:

        font = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX

        text = "Height : "+ str(cap.get(4)) + "Width : "+ str(cap.get(3))

        date_time = str(datetime.datetime.now())        
        frame = cv2.putText(frame, date_time, (10,50), font, 1, (255,0,255),2,cv2.LINE_AA)
        cv2.imshow("Video", frame)

        if cv2.waitKey(1) and 0xFF == ord("e"):
            break

    else:
        break
cap.release()
cv2.destroyAllWindows()