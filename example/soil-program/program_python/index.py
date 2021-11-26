import pyrebase
import serial
import json
import os
from datetime import datetime
from time import sleep

# variabel koneksi usb arduino
usb_port = "COM4"

# Konfigurasi Alamat Firebase Database
firebaseConfig = {
    "apiKey": "AIzaSyCC9E5L0365-sWBNZ4JAtgsitFSJuEkCH8",
    "authDomain": "kroeng-a879b.firebaseapp.com",
    "databaseURL": "https://kroeng-a879b-default-rtdb.firebaseio.com",
    "projectId": "kroeng-a879b",
    "storageBucket": "kroeng-a879b.appspot.com",
    "messagingSenderId": "1073718373043",
    "appId": "1:1073718373043:web:1104d5c184e541a1949ec6",
    "measurementId": "G-YFHZQHXDCN"
};

# Clear terminal
if(os.name == 'nt'):
    os.system('cls')
else:
    os.system('clear')

# Program relay
def Relay():
    # Mengambil status relay di database
    saklar_status = db.child("Led_App_Debug_copy").child("saklar_status").child("aksi").get().val()
    auto_saklar_status = db.child("Led_App_Debug_copy").child("saklar_oto").child("aksi").get().val()

    # Mengambil data kelembaban
    data = db.child("Data-sensor").child("kelembaban").get().val()
    data = int(data)

    # Program relay
    if(saklar_status == "1"):
        port.write(bytes('1','utf-8'))
        print("Saklar Hidup")
            
    elif(saklar_status == "0"):
        port.write(bytes('0','utf-8'))
        print("Saklar mati")

    # Program auto relay
    if(auto_saklar_status == "1"):
        if(data >= 75): # Jika data lebih dari 75%
            db.child("Led_App_Debug_copy").child("saklar_status").child("aksi").set("1")
            port.write(bytes('1', 'utf-8'))
        
        elif(data <= 75): # Jika data kurang dari 75%
            db.child("Led_App_Debug_copy").child("saklar_status").child("aksi").set("0")
            port.write(bytes('0', 'utf-8'))
    
    elif(auto_saklar_status == "0"):
        db.child("Led_App_Debug_copy").child("saklar_oto").child("aksi").set("0")
        
# Program Main
if __name__ == "__main__":
    # Konfigurasi USB Arduino Serial Port
    port = serial.Serial(
        port=usb_port, 
        baudrate=9600, 
        timeout=1
        )

    # Membuat object database
    firebase = pyrebase.initialize_app(firebaseConfig)
    db = firebase.database()
    
    while True:
        try:
            # Mengambil data serial arduino
            data_arduino = port.readline()
            data_arduino = data_arduino.decode()
            print(data_arduino)
            
            sleep(0.5)
            # Mengambil data serial arduino didalam json
            data = json.loads(data_arduino)
            # Memasukan data ke dalam variabel kelembaban
            kelembaban = int(data["kelembaban"])
        
            # Tanggal dan Waktu
            now = datetime.now()
            waktu = now.strftime("%H:%M:%S")
            tanggal = now.day
            bulan = now.month
            tahun = now.year
            date_time = str(f"{tanggal}-{bulan}-{tahun}({waktu})")

            # Kirim data ke firebase real-time database
            db.child("Data-sensor").child("tanggal-waktu").set(date_time)
            db.child("Data-sensor").child("kelembaban").set(kelembaban)
            
            # Reset input buffer arduino
            port.reset_input_buffer()

            # Jalankan Program Relay
            Relay()
            
        except:
            None

