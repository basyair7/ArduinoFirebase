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
    "apiKey": "",
    "authDomain": "",
    "databaseURL": "",
    "projectId": "",
    "storageBucket": "",
    "messagingSenderId": "",
    "appId": "",
    "measurementId": ""
};

# Clear terminal
if(os.name == 'nt'):
    os.system('cls')
else:
    os.system('clear')

# Program relay
def Relay():
    # Mengambil status relay di database
    saklar_status = db.child("saklar_status").child("aksi").get().val()
    auto_saklar_status = db.child("saklar_oto").child("aksi").get().val()

    # Mengambil data kelembaban
    data = db.child("Data_sensor").child("Kelembaban").get().val()
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
            db.child("saklar_status").child("aksi").set("1")
            port.write(bytes('1', 'utf-8'))
        
        elif(data <= 75): # Jika data kurang dari 75%
            db.child("saklar_status").child("aksi").set("0")
            port.write(bytes('0', 'utf-8'))
    
    elif(auto_saklar_status == "0"):
        db.child("saklar_oto").child("aksi").set("0")
        
# Program Main
if __name__ == "__main__":
    # Konfigurasi Alamat USB Arduino Serial Port
    port = serial.Serial(
        port=usb_port, 
        baudrate=9600, #utk kecepatan kirim dan terima data dalam 9660 bit per detik.
        timeout=1 #set batas maks waktu tunggu transmisi data.
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
        
            # Memuat Tanggal dan Waktu
            now = datetime.now()
            waktu = now.strftime("%H.%M.%S")
            tanggal = now.day
            bulan = now.month
            tahun = now.year
            date_time = str(f"{tanggal}-{bulan}-{tahun}({waktu})")

            # Kirim data ke firebase real-time database
            db.child("Data_sensor").child("Tanggal_waktu").set(date_time)
            db.child("Data_sensor").child("Kelembaban").set(kelembaban)
            
            # membersihkan data masuk pada serial arduino
            port.reset_input_buffer()

            # Jalankan Program Relay
            Relay()
            
        except:
            None

