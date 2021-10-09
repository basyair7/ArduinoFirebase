#include <ArduinoJson.h>

// definisi pin
#define soil_sensor A0
#define relay 4

void setup(){
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial.setTimeout(1);
  // deklarasi dari pin relay
  relay_pin(relay);
  
  // konfigurasi pin sensor
  pinMode(soil_sensor, INPUT);
  
}

void loop(){
  // put your main code here, to run repeatedly:
  // Membuat objek jsonBuffer
  StaticJsonBuffer<200> jsonBuffer;
  JsonObject& data = jsonBuffer.createObject();
  
  // Membuat & mengisi nilai variabel data soil sensor
  int data_soil = map(analogRead(soil_sensor), 0, 1023, 0, 100);
  
  // Masukkan data ke dalam array 
  data["kelembaban"] = data_soil;
  
  // Mengirim data ke Serial
  data.printTo(Serial);
  // Bersihkan json jika data telah terkirim
  jsonBuffer.clear();
  Serial.println();
  
  // Memanggil program relay
  relay_1(relay);
  
  delayMicroseconds(500);
}
  
