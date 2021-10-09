import pyrebase
import serial
import json
import os
from datetime import datetime

# clear terminal
if(os.name == 'nt'):
    os.system('cls')
else:
    os.system('clear')

while True:

    try:
        # Arduino config
        arduinoConfig = serial.Serial("COM2", 9600);

        # Firebase Config
        firebaseConfig = {
            "apiKey": "AIzaSyBMAimWv9f5hzo2KzT-vfUPIl19gWVzzJM",
            "authDomain": "dht-proteus.firebaseapp.com",
            "databaseURL": "https://dht-proteus-default-rtdb.asia-southeast1.firebasedatabase.app/",
            "projectId": "dht-proteus",
            "storageBucket": "dht-proteus.appspot.com",
            "messagingSenderId": "264187239063",
            "appId": "1:264187239063:web:a9e578b4d81f49dfbc67d2",
            "measurementId": "G-GJEKN4PYYR"
        };

        firebase = pyrebase.initialize_app(firebaseConfig)
        db = firebase.database()

        while True:
            # get data arduino
            data_dht = arduinoConfig.readline()
            data_dht = data_dht.decode("utf-8")

            # get data json
            data = json.loads(data_dht)
            # insert in variable
            celcius = data["celcius"]
            fahrenheit = data["fahrenheit"]
            humidity = data["kelembaban"]
            
            # date time
            now = datetime.now()
            waktu = now.strftime("%H:%M")
            tanggal = now.day
            bulan = now.month
            tahun = now.year
            date_time = f"{tanggal}-{bulan}-{tahun}({waktu})"

            # print
            print(f"Temperature : {celcius}*C ({fahrenheit}*F)\nHumidity : {humidity}%")

            #upload data to firebase
            db.child("data_sensor").child("tanggal-waktu").set(date_time)
            db.child("data_sensor").child("kelembaban").set(humidity)
            db.child("data_sensor").child("celcius").set(celcius)
            db.child("data_sensor").child("fahrenheit").set(fahrenheit)

    except:
        None
