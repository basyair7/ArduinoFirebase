#include <ESP8266WiFi.h>
#include <SoftwareSerial.h>
#include <ArduinoJson.h>
#include <FirebaseESP8266.h>

#define lv_kelembaban_1 50
#define lv_kelembaban_2 50
#define lv_kelembaban_3 50
#define lv_kelembaban_4 50

#define D7 (13)
#define WIFI_SSID "@wifi07.id"
#define WIFI_PASSWORD "87654321"
#define FIREBASE_HOST "awp-db-default-rtdb.firebaseio.com"
#define FIREBASE_AUTH "s4NukWOoYfjAMsuikEci9ShveUiWltOGsRpOGEx1"


FirebaseData firebaseData; //firebase function
SoftwareSerial nano_board(D6, D5); //D6 = Rx and D5 = Tx

String path_relay = "saklar_status/aksi";
String path_sensor = "data_sensor";
String path_relay_auto = "saklar_oto/aksi";
int pinRelay = D7;
int countval = 0;

//void ICACHE_RAM_ATTR loop(); // jika nodemcu intrrupt

void setup() {
  Serial.begin(115200);
  // setup pin relay
  pinMode(pinRelay, OUTPUT);
  digitalWrite(pinRelay, HIGH);
  // setup wifi connection
  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
  Serial.print("Connecting");
  while (WiFi.status() != WL_CONNECTED) {
    //Serial.print(".");
    delay(500);
  }
  Serial.println();
  Serial.println("Connected.");
  // Setup firebase auth & host link
  Firebase.begin(FIREBASE_HOST, FIREBASE_AUTH);
  //Firebase.reconnectWiFi(true);
  //firebaseData.setBSSLBufferSize(1024, 1024);
  //firebaseData.setResponseSize(1024);
  Firebase.setReadTimeout(firebaseData, 1000 * 60);
  //Firebase.setwriteSizeLimit(firebaseData, "tiny");
  
  nano_board.begin(9600);
  while (!Serial) continue;
  set_data_sensor();
  
}

void loop() {
  // get data from arduino
  StaticJsonBuffer<1000> jsonBuffer;
  JsonObject& data = jsonBuffer.parseObject(nano_board);
  if (data == JsonObject::invalid()){
    jsonBuffer.clear();
    return;
  }

  String getdata_1 = data["kelembaban_1"];
  String getdata_2 = data["kelembaban_2"];
  String getdata_3 = data["kelembaban_3"];
  String getdata_4 = data["kelembaban_4"];
  String getdata_5 = data["curah_hujan"];
  int getdataint_1 = data["kelembaban_1"];
  int getdataint_2 = data["kelembaban_2"];
  int getdataint_3 = data["kelembaban_3"];
  int getdataint_4 = data["kelembaban_4"];
  int getdataint_5 = data["curah_hujan"];
   
  // Get action relay status
  if(Firebase.get(firebaseData, path_relay)){
    if(firebaseData.dataType() == "string"){
      String relay = firebaseData.stringData();
      if(relay == "1"){
        digitalWrite(pinRelay,LOW);
      }
      else if(relay == "0"){
        digitalWrite(pinRelay,HIGH);
      }
    }
  }
  
  // Push data in database
  Firebase.setString(firebaseData, path_sensor + "/kelembaban_1", getdata_1);
  delay(5);
  Firebase.setString(firebaseData, path_sensor + "/kelembaban_2", getdata_2);
  delay(5);
  Firebase.setString(firebaseData, path_sensor + "/kelembaban_3", getdata_3);
  delay(5);
  Firebase.setString(firebaseData, path_sensor + "/kelembaban_4", getdata_4);
  delay(5);
  Firebase.setString(firebaseData, path_sensor + "/curah_hujan", getdata_5);
  delay(5);

  if(Firebase.get(firebaseData, path_relay_auto)) {
    if(firebaseData.dataType() == "string") {
      String relay_auto = firebaseData.stringData();
      if(relay_auto == "1") {
        if(getdataint_1 >= lv_kelembaban_1 && getdataint_2 >= lv_kelembaban_2 && getdataint_3 >= lv_kelembaban_3 && getdataint_4 >= lv_kelembaban_4) {
          countval++;
        }
        else if(getdataint_1 <= lv_kelembaban_1 && getdataint_2 <= lv_kelembaban_2 && getdataint_3 <= lv_kelembaban_3 && getdataint_4 <= lv_kelembaban_4){
          digitalWrite(pinRelay, HIGH);
          countval = 0;
          Firebase.setString(firebaseData, path_relay, "0"); 
        }
      }
      else if(relay_auto == "0"){
        countval = 0;
      }
    }
  }

  if (countval >= 2) {
    digitalWrite(pinRelay, LOW);
    Firebase.setString(firebaseData, path_relay, "1");
  }
  
  //jsonBuffer.clear();
  delay(15);
}

void set_data_sensor() {
  Firebase.setString(firebaseData, path_sensor + "/kelembaban_1", "0");
  Firebase.setString(firebaseData, path_sensor + "/kelembaban_2", "0");
  Firebase.setString(firebaseData, path_sensor + "/kelembaban_3", "0");
  Firebase.setString(firebaseData, path_sensor + "/kelembaban_4", "0");
  Firebase.setString(firebaseData, path_sensor + "/curah_hujan", "0");
  delay(5);
}
