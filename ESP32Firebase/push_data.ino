#define delay_1 10000 // ms
#define delay_2 10000 // ms
unsigned long waktu_sebelum_kirim = 0;
unsigned long waktu_sebelum_terima = 0;

void push_data(int data_1, int data_2, int data_3, int data_4)
{
  unsigned long waktu_sekarang = millis();

  if((unsigned long) (waktu_sekarang - waktu_sebelum_kirim) >= delay_1)
  {
    waktu_sebelum_kirim = waktu_sekarang;
    // Push data in database
    Firebase.setInt(firebaseData, path_1, data_1);
    delay(5);
    Firebase.setInt(firebaseData, path_2, data_2);
    delay(5);
    Firebase.setInt(firebaseData, path_3, data_3);
    delay(5);
    Firebase.setInt(firebaseData, path_4, data_4);
    delay(10);
  }
}

void program_relay(int pinout)
{
  unsigned long waktu_sekarang = millis();
  if((unsigned long) (waktu_sekarang - waktu_sebelum_terima) >= delay_2)
  {
    // program relay
    bool kondisi_kran;
    Firebase.getBool(firebaseData, path_kran, &kondisi_kran);
    if(kondisi_kran == true)
    {
      digitalWrite(pinout, HIGH);
    }
    else
    {
      digitalWrite(pinout, LOW);
    }
  }
}

void set_data_sensor(String path)
{
  Firebase.setInt(firebaseData, path, 0);
  delay(10);
}