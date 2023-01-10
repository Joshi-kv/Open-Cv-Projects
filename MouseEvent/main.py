import cv2

#creating function to draw shape when button click
def draw(event,x,y,flag,parameter):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(image,(x,y),20,(255,0,0),-1)
image=cv2.imread('Images/iphone-14.jpg',1)
cv2.imshow('Image',image)
cv2.setMouseCallback('Image',draw)
while (True):
    cv2.imshow('Image',image)
    if cv2.waitKey(20) & 0xFF==27:
        break
cv2.destroyAllWindows()