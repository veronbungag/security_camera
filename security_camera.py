import cv2
import time
import datetime

cap = cv2.VideoCapture(o)

while True:
    _, frame = cap.read()
    
