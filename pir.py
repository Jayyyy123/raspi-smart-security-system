import RPi.GPIO as GPIO
import time
import numpy as np
import cv2
import os
from time import sleep
from datetime import datetime


# FaceCcascade
faceCascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
cap.set(3, 640)  # set Width
cap.set(4, 480)  # set Height


# set GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(20, GPIO.IN)  # PIR
GPIO.setup(19, GPIO.OUT)  # BUzzer


def face_recog():

    count = 0
    while True:
        ret, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.2,
            minNeighbors=5,
            minSize=(20, 20)
        )

        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
            count += 1
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = img[y:y+h, x:x+w]

            now = datetime.now()
            dt = now.strftime("%d%m%Y%H:%M:%S")
            name = dt+".jpg"
            cv2.imwrite(name, img)
            uploadImage = storage.child(name).put(name)
            print("Image sent")

        cv2.imshow('video', img)
        k = cv2.waitKey(30) & 0xff
        if k == 27:  # press 'ESC' to quit
            break
        elif count >= 10:
            print("Face recogntiion done")
            break

    cap.release()
    cv2.destroyAllWindows()


# Initialize
try:
    time.sleep(2)  # to stabilize sensor
    while True:
        if GPIO.input(20):
            GPIO.output(19, False)
            time.sleep(0.5)  # Buzzer turns on for 0.5 sec
            GPIO.output(19, True)
            print("Motion Detected...")
            face_recog()
            time.sleep(5)  # to avoid multiple detection
        time.sleep(0.1)  # loop delay, should be less than detection delay

except:
    GPIO.cleanup()
