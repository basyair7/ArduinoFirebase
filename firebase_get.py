import pyrebase
from datetime import datetime
from time import sleep

# Firebase
firebaseConfig = {
  "apiKey": "AIzaSyAfb-5SyAnuG7qMtUb09Uz-wBBJ6Xq_HUM",
  "authDomain": "arduinofirebase-ef1e4.firebaseapp.com",
  "databaseURL": "https://arduinofirebase-ef1e4-default-rtdb.firebaseio.com/",
  "projectId": "arduinofirebase-ef1e4",
  "storageBucket": "arduinofirebase-ef1e4.appspot.com",
  "messagingSenderId": "56550174951",
  "appId": "1:56550174951:web:0cf46860e7285b9bb03242",
  "measurementId": "G-SNRHXMM3F5"
}

firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()

for i in range(10):
    now = datetime.now()
    waktu = (now.strftime("%H:%M:%S"))
    tanggal = now.day
    bulan = now.month
    tahun = now.year
    date_time = f"{tanggal}-{bulan}-{tahun}({waktu})"

    data_sensor = db.child("data_sensor").get().val()

    print(data_sensor)
    