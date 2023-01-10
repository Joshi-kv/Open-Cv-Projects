import cv2
image=cv2.imread('Images/iphone-14.jpg')
cv2.rectangle(image,(0,0),(100,100),(255,0,0),5)
cv2.imshow('Shape',image)
cv2.waitKey(0)
cv2.destroyAllWindows()