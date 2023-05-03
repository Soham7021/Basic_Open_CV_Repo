import cv2

img = cv2.imread("messi5.jpg",1)
# Drawing a line on a Image

img = cv2.line(img, (0,0), (255,255), (102,153,255),10)
# cv2.line(image,pint1,pnt2,colour,thickness) for color in rgb go on rgb color picker websiite and print ulta

#Drawing a arrowed line
img = cv2.arrowedLine(img, (0,255), (255,255), (0,255,0),10)

#Drawing rectangele
img = cv2.rectangle(img, (384,0), (510,128), (0,0,255),20)#if we put "-1" instead of 20 it will fill the box with that color

#Drawing a Circle
img = cv2.circle(img, (447,63), 63, (0,255,0),-1)

#Writing a text on the Image
font = cv2.FONT_HERSHEY_COMPLEX
img = cv2.putText(img, "Open CV", (10,320), font, 2, (0,255,255),10,cv2.LINE_AA)
#cv2.putText(image,sentence,starting point,font , font size,color,Thickness,line Type)

cv2.imshow("image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()