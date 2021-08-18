import numpy as np
import cv2
import os
import pyrebase
from time import sleep
from datetime import datetime

firebaseConfig = {
    "apiKey": "AIzaSyBIQCVPX9XTj3E_F63AT-IeRC98E1eS6LE",
    "authDomain": "images-6ed75.firebaseapp.com",
    "databaseURL": "https://images-6ed75-default-rtdb.firebaseio.com",
    "projectId": "images-6ed75",
    "storageBucket": "images-6ed75.appspot.com",
    "messagingSenderId": "596047942745",
    "appId": "1:596047942745:web:24486887830112003ecd48",
    "measurementId": "G-H1QK3VQ910",
}

firebase_storage = pyrebase.initialize_app(firebaseConfig)
storage = firebase_storage.storage()


faceCascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
cap.set(3, 640)  # set Width
cap.set(4, 480)  # set Height


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

cap.release()
cv2.destroyAllWindows()
