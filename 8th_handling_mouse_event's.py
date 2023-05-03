import numpy as np
import cv2

events = [i for i in dir(cv2) if 'EVENT' in i ]
#dir shows all the classes and the functions inside the cv2 it is basically inbuilt function
#where 'EVENT' is all the mouse events available in the cv2 module
print(events)

def click_event(event,x,y,flags,param):#this is standard form for  the click events

    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, ', ', y)#i.e the co-ordinates of the point on the image we are clicking
        font = cv2.FONT_HERSHEY_COMPLEX
        strXY = str(x) + " ," + str(y)
        cv2.putText(img, strXY, (x,y),font,.5, (255,255,0), 2)
        cv2.imshow('image', img)

    if event == cv2.EVENT_LBUTTONDBLCLK:
        font = cv2.FONT_HERSHEY_COMPLEX
        strsomething = "This is messis image"
        cv2.putText(img, strsomething, (10,50), font,.7, (255,0,255),2)#2 is thickness
        cv2.imshow('image',img)

    if event == cv2.EVENT_RBUTTONDOWN:
        blue = img[y,x,0] #so for blue its zero
        green = img[y,x,1]
        red = img[y,x,2]
        font = cv2.FONT_HERSHEY_COMPLEX
        strBGR = str(blue) + " ," + str(green)+" , "+ str(red)
        cv2.putText(img, strBGR, (x,y),font,.5, (255,277,310), 2)
        cv2.imshow('image', img)
    #this is to get the colur code of the image where we left double click
#//
#img = np.zeros([512,512,3],np.uint8)#this is for creating the blank image refer the 5th practice creating blank 
#//
# image.py
# we can do it by taking the new image for ex.
img = cv2.imread("messi5.jpg ", 1)
cv2.imshow('image', img)
cv2.setMouseCallback('image', click_event)
#cv2.setMouseCallback('name of image',def function i.e click event())
#we use this to call the def click event i.e if we click as per assigned so it will work

cv2.waitKey(0)
cv2.destroyAllWindows()