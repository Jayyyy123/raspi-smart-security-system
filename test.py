import pyrebase

firebaseConfig = { 
    "apiKey": "AIzaSyBG6ZzJwFTR0yLrdpAHsZUGY7lWYQeoOo0",
    "authDomain": "rpi-image-bec1b.firebaseapp.com",
    "databaseURL": "https://rpi-image-bec1b-default-rtdb.asia-southeast1.firebasedatabase.app",
    "projectId": "rpi-image-bec1b",
    "storageBucket": "rpi-image-bec1b.appspot.com",
    "messagingSenderId": "382483561782",
    "appId": "1:382483561782:web:213ce79e21fe14cb3d4797",
    "measurementId": "G-MVV0HJDG34",
    "serviceAccount": "serviceAccountKey.json"
}

firebase_storage = pyrebase.initialize_app(firebaseConfig)
storage = firebase_storage.storage()

storage.child("0906202122:13:44.jpg").put("0906202122:13:44.jpg")

