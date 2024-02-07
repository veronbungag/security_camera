import cv2
import time
import datetime

cap = cv2.VideoCapture(o)

while True:
    _, frame = cap.read()
    
    cv2.imshow("Kids Camera", frame)
    
    if cv2.waitKey(1) == ord('q')
        break
