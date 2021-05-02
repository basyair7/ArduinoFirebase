from random import randint
from datetime import datetime
import pyrebase
import time
num_save = 1
firebaseConfig = {
    "apiKey": "AIzaSyDb7uvq_45rQPS7Je7amnGhMXevdZgz4Nk",
    "authDomain": "testing-db1237.firebaseapp.com",
    "databaseURL": "https://testing-db1237-default-rtdb.firebaseio.com",
    "projectId": "testing-db1237",
    "storageBucket": "testing-db1237.appspot.com",
    "messagingSenderId": "332796751686",
    "appId": "1:332796751686:web:538a66c90c010ce7a6bf47",
    "measurementId": "G-S7KPWECYDN"
    }

firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()

while True:
    temp = randint(19,32)
    hum = randint(75,90)

    now = datetime.now()
    date = now.day
    month = now.month
    year = now.year
    date_time = f"{date}-{month}-{year}"

    db.child("data_sensor").child(date_time).child("temperature").set(temp)
    db.child("data_sensor").child(date_time).child("humidity").set(hum)
    
    num_save += 1
    time.sleep(5)

