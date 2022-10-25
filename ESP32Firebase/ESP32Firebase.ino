/* Program Firebase ESP32 dengan sensor soil moisture
 * reference : https://youtu.be/T5wYT5IT0fI
 */
#include <WiFi.h>
#include <FirebaseESP32.h>

// provide the token generation process info.
#include <addons/TokenHelper.h>

// provide the RTDB payload printing info and other helper functions.
#include <addons/RTDBHelper.h>

// define pin sensor
#define sensor_kelembaban_1 13
#define sensor_kelembaban_2 12
#define sensor_kelembaban_3 14
#define sensor_kelembaban_4 27
#define pin_relay 26

#define lv_kelembaban_1 50
#define lv_kelembaban_2 50
#define lv_kelembaban_3 50
#define lv_kelembaban_4 50

// root json firebase data
const String path_1 = "data_sensor/kelembaban_1";
const String path_2 = "data_sensor/kelembaban_2";
const String path_3 = "data_sensor/kelembaban_3";
const String path_4 = "data_sensor/kelembaban_4";
const String path_kran = "saklar_kran/kran";


// 1. Define the WiFi Credentials
#define WIFI_SSID ""
#define WIFI_PASS ""

// For the following credentials, see examples/Authentications/SignInAsUser/EmailPassword/EmailPassword.ino

// 2. Define the API Key
#define API_KEY "API_KEY"

// 3. Define the RTDB URL
#define DATABASE_URL "URL"

// 4. Defin ethe user email and password that already register or added in yout project
#define USER_EMAIL "USER_EMAIL"
#define USER_PASSWORD "USER_PASSWORD"

// Define Firebase data object
FirebaseData firebaseData;

FirebaseAuth auth;
FirebaseConfig config;

const char* ssid = WIFI_SSID;
const char* password = WIFI_PASS;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(pin_relay, OUTPUT);
  pinMode(sensor_kelembaban_1, INPUT);
  pinMode(sensor_kelembaban_2, INPUT);
  pinMode(sensor_kelembaban_3, INPUT);
  pinMode(sensor_kelembaban_4, INPUT);

  // delete old config
  WiFi.disconnect();
  delay(1000);

  WiFi.onEvent(WiFiStationConnected, SYSTEM_EVENT_STA_CONNECTED);
  WiFi.onEvent(WiFiGotIP, SYSTEM_EVENT_STA_GOT_IP);
  WiFi.onEvent(WiFiStationDisconnected, SYSTEM_EVENT_STA_DISCONNECTED);

  WiFi.begin(ssid, password);
  Serial.println();

  // Assign the user sign in credentials
  auth.user.email = USER_EMAIL;
  auth.user.password = USER_PASSWORD;

  // Assign the RTDB URL (required)
  config.database_url = DATABASE_URL;

  // Assign the callback function for the long running token generation task
  config.token_status_callback = tokenStatusCallback; // see addons/TokenHelper.h

  Firebase.begin(&config, &auth);
  Firebase.reconnectWiFi(true);
  Firebase.setDoubleDigits(5);
  
  set_data_sensor(path_1);
  set_data_sensor(path_2);
  set_data_sensor(path_3);
  set_data_sensor(path_4);

}

void loop() {
  // put your main code here, to run repeatedly:
  // mapping data sensor
  int val_1 = map(analogRead(sensor_kelembaban_1), 0, 4095, 0, 100);
  int val_2 = map(analogRead(sensor_kelembaban_2), 0, 4095, 0, 100);
  int val_3 = map(analogRead(sensor_kelembaban_3), 0, 4095, 0, 100);
  int val_4 = map(analogRead(sensor_kelembaban_4), 0, 4095, 0, 100);

  // kirim data ke firebase
  push_data(val_1, val_2, val_3, val_4);
  
  // run program relay
  program_relay(pin_relay);
  
}
