import cv2
capture=cv2.VideoCapture(0)
while True:
    ret,frame=capture.read(0)
    cv2.imshow('video',frame)
    #condition for exit window
    if cv2.waitKey(1) & 0xFF==27: 
        break
capture.release()
cv2.destroyAllWindows()