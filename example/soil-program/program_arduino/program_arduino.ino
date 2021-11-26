#include <ArduinoJson.h>

// definisi pin sensor
#define soil_sensor A0
#define relay 4

void setup() {
  // put your setup code here, to run once:
  
  Serial.begin(9600); 
  //utk kecepatan kirim dan terima data dalam 9660 bit per detik.
  
  Serial.setTimeout(1); 
  //set batas maks waktu tunggu transmisi data.
  
  //konfigurasi/set pin yang bekerja pada posisi in atau out
  relay_pin(relay); 
  pinMode(soil_sensor, INPUT);

}

void loop() {
  // put your main code here, to run repeatedly:
  // Program mengambil data sensor
  // Membuat pohon objek staticJsonBuffer utk menyimpan data
  StaticJsonBuffer<200> jsonBuffer;
  
  // Membuat akar untuk mengisi nilai sensor
  JsonObject& data = jsonBuffer.createObject();

  // mengubah data sinyal analog 0-1023 ke 0-100
  int nilaiSoil = map(analogRead(soil_sensor), 0, 1023, 0, 100);

  // masukkan nilai sensor ke akar data
  data["kelembaban"] = nilaiSoil;

  // kirim data pohon ke serial
  data.printTo(Serial);

  // Bersihkan data pohon
  jsonBuffer.clear();
  Serial.println();

  //memanggil fungsi relay
  relay_2(relay);

  delayMicroseconds(500);

}
