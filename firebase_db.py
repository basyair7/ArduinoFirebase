# Arduino Firebase realtime
import pyrebase
import serial
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
# Arduino
board = serial.Serial("COM7", 9600)

for i in range(10):
    data_dht = board.readline()
    decode_value = str(data_dht[0:len(data_dht)].decode("utf-8"))

    now = datetime.now()
    waktu = (now.strftime("%H:%M:%S"))
    tanggal = now.day
    bulan = now.month
    tahun = now.year
    date_time = f"{tanggal}-{bulan}-{tahun}({waktu})"

    db.child("data_sensor").child(date_time).set(decode_value)
    #db.child("data_sensor").remove()
    
