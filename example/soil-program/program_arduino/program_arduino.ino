#include <ArduinoJson.h>

// definisi pin sensor
#define soil_sensor A0
#define relay 4

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial.setTimeout(1);
  relay_pin(relay);
  pinMode(soil_sensor, INPUT);

}

void loop() {
  // put your main code here, to run repeatedly:
  // Program mengambil data sensor
  StaticJsonBuffer<200> jsonBuffer;
  JsonObject& data = jsonBuffer.createObject();
  
  int nilaiSoil = map(analogRead(soil_sensor), 0, 1023, 0, 100);

  data["kelembaban"] = nilaiSoil;

  data.printTo(Serial);
  jsonBuffer.clear();
  Serial.println();

  relay_2(relay);

  delayMicroseconds(500);

}
