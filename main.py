from Google import Create_Service
from googleapiclient.http import MediaFileUpload
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

CLIENT_SECRET_FILE = 'client_secret_928305625059-ilfpsogk9rgm774cl8kqrei6qbi47c57.apps.googleusercontent.com.json'
API_NAME = 'drive'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/drive']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

folder_id = '1j44Fz9O0H0zhLWhZv5N-kLfXxQpJiB6M'


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
            file_name = dt + ".jpg"
            cv2.imwrite(file_name, img)
            mime_types = 'image/jpeg'
            file_metadata = {
                'name': file_name,
                'parents': [folder_id]
            }

            media = MediaFileUpload('{0}'.format(
                file_name), mimetype=mime_types)

            service.files().create(
                body=file_metadata,
                media_body=media,
                fields='id'
            ).execute()
            print("Image sent")

        cv2.imshow('video', img)
        k = cv2.waitKey(30) & 0xff
        if k == 27:  # press 'ESC' to quit
            break
        elif count >= 10:
            print("Count end")
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
            print("Face Recognition done")
            break  # to avoid multiple detection
        time.sleep(0.1)  # loop delay, should be less than detection delay

except:
    GPIO.cleanup()


# file_name = 'test.jpg'
# mime_types = 'image/jpeg'

# file_metadata = {
#     'name': file_name,
#     'parents': [folder_id]
# }

# media = MediaFileUpload('{0}'.format(file_name), mimetype=mime_types)

# service.files().create(
#     body=file_metadata,
#     media_body=media,
#     fields='id'
# ).execute()
