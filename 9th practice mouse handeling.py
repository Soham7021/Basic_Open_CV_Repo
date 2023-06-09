import numpy as np
import cv2


def click_event(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x, y), 3,(0,0,255),-1)
        points.append((x,y))
        if len(points) >=2:
            cv2.line(img, points[-1], points[-2], (255,255,255),5)

            cv2.imshow('image', img) 

    if event == cv2.EVENT_RBUTTONDOWN:
        blue = img[x,y,0]
        green = img[x,y,1]
        red = img[x,y,2]
        cv2.circle(img, (x,y), 3, (0,0,255),-1)
        mycolorimage = np.zeros((512,512,3),np.uint8)

        mycolorimage[:]  = [blue,green,red]
        cv2.imshow('color',mycolorimage)


img = cv2.imread("messi5.jpg")
cv2.imshow('image', img)
points = []
cv2.setMouseCallback('image', click_event)

cv2.waitKey()
cv2.destroyAllWindows()