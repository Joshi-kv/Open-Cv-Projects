import cv2
image=cv2.imread('Images/iphone-13.jpg',1)
cv2.imshow("Iphone",image)
cv2.waitKey(10000)
cv2.destroyAllWindows()