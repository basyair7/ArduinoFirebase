from datetime import datetime
from time import sleep
import pyrebase
import serial
import json
import os

# Clear terminal
if(os.name == 'nt'):
  os.system('cls')
else:
  os.system('clear')

# Program relay
def Relay():
  # Mengambil status relay di database
  saklar_status = db.child("saklar_status").child("aksi").get().val()
  auto_saklar_status = db.chil("saklar_oto").child("aksi").get().val()
  
  # Mengambil data kelembaban 
  data = db.child("data_sensor").child("kelembaban").get().val()
  data = int(data)
  
  # Program relay
  if(saklar_status == "1"):
    port.write(bytes('1', 'utf-8'))
    print("Saklar Hidup")
    
  elif(saklar_status == "0"):
    port.write(bytes('0', 'utf-8'))
    print("Saklar Mati")
  
  # Program auto relay
  if(auto_saklar_status == "1"):
    if(data >=75): # Jika data lebih besar dari 75%
      db.child("saklar_status").child("aksi").set("1")
      port.write(bytes('1', 'utf-8'))
    
    elif(data <= 75): # Jika data kurang besar dari 75%
      db.child("saklar_status").child("aksi").set("0")
      port.write(bytes('0', 'utf-8'))
      
  elif(auto_saklar_status == "0"):
    db.child("saklar_oto").child("aksi").set("0")
 
# Program Main
if __name__ == "__main__":
  # Konfigurasi Arduino Serial Port
  port = serial.Serial(
    port="COM4",
    baudrate=9600,
    timeout=1
  )
  
  # Konfigurasi Firebase Database
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
  
  # Membuat object database
  firebase = pyrebase.initialize_app(firebaseConfig)
  db = firebase.database()
  
  while True:
    try:
      # Mengambil data serial arduino 
      data_arduino = port.readline()
      data_arduino = data_arduino.decode('utf-8')
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
      db.child("data_sensor").child("tanggal-waktu").set(date_time)
      db.child("data_sensor").child("kelembaban").set(kelembaban)
      
      # Reset input buffer serial port
      port.reset_input_buffer()
      
      # Memanggil Program Relay
      Relay()
      
    except:
      None
