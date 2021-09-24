import pyrebase
from datetime import datetime
from time import sleep

# Firebase
firebaseConfig = {
  "apiKey": "",
  "authDomain": "",
  "databaseURL": "",
  "projectId": "",
  "storageBucket": "",
  "messagingSenderId": "",
  "appId": "",
  "measurementId": ""
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
    
