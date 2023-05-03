import cv2
cap = cv2.VideoCapture(0)
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
#Insted of "cv2.CAP_PROP_FRAME_HEIGHT" we can write 4
#Insted of "cap.get(cv2.CAP_PROP_FRAME_WIDTH" we can write 3
#something different than before


#///***{
cap.set(4, 720)#where 4 represent height"cv2.CAP_PROP_FRAME_HEIGHT"
cap.set(3, 1280)#where 3 represents widht "cv2.CAP_PROP_FRAME_WIDTH"

print(cap.get(4))
print(cap.get(3))
#if the parameters are not given properly computer will display video in default paramertrs and if the givn values are so high then it will display video in default max
# }///***



while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        cv2.imshow("Video", frame)

        if cv2.waitKey(1) and 0xFF == ord("e"):
            break

    else:
        break
cap.release()
cv2.destroyAllWindows()