import cv2
import numpy as np 

def nothing(x):
    pass

cv2.namedWindow('Tracking')
#this is to create the trackbar to identify the range of the color that we want for that look at the line beloaw athat shows the l_b and u_b which has some ranges

cv2.createTrackbar('LH', 'Tracking', 0, 255, nothing)
cv2.createTrackbar('LS', 'Tracking', 0, 255, nothing)
cv2.createTrackbar('LV', 'Tracking', 0, 255, nothing)
cv2.createTrackbar('UH', 'Tracking', 255, 255, nothing)
cv2.createTrackbar('US', 'Tracking', 255, 255, nothing)
cv2.createTrackbar('UV', 'Tracking', 255, 255, nothing)


while True:
    frame = cv2.imread('colorballs.jpg')

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)#this is to target any specific color in this case it blue shon below as l_b and u_b

    l_h = cv2.getTrackbarPos('LH', 'Tracking')
    l_s = cv2.getTrackbarPos('LS', 'Tracking')
    l_v = cv2.getTrackbarPos('LV', 'Tracking')

    u_h = cv2.getTrackbarPos('UH', 'Tracking')
    u_s = cv2.getTrackbarPos('US', 'Tracking')
    u_v = cv2.getTrackbarPos('UV', 'Tracking')

    #now using above 6line we will not have to give values to l_b and u_b as we will directly assigned them on the window

    l_b = np.array([l_h,l_s,l_v])
    u_b = np.array([u_h,u_s,u_v])




#l_b and u_b are the ranges of the blue color which we are going to target

    mask = cv2.inRange(hsv, l_b, u_b)
    #this is to specify the range of blue color from l_b to u_b thus it is used for geting only items with blue color

    res = cv2.bitwise_and(frame, frame, mask=mask)#both the sources are same because we have to get the blue are from the same image

    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)

    key = cv2.waitKey(1)
    if key == 27:
        break

cv2.destroyAllWindows()