int relay_pin(int pin){
  //konfigurasi/set pin yang bekerja pada posisi in atau out
  pinMode(pin, OUTPUT);
  // kembalikan nilai pin
  return(pin);
}

void relay_1(int pin){
  // Program relay 
  // membaca aksi dari program python
  int aksi = Serial.read();

  if(aksi == '1'){
    digitalWrite(pin, LOW); // saklar hidup
  }
  else if(aksi == '0'){
    digitalWrite(pin, HIGH); //saklar mati
  }
}

void relay_2(int pin){
  // Program relay for proteus
  // membaca aksi dari program python
  int aksi = Serial.read();

  if(aksi == '1'){
    digitalWrite(pin, HIGH); //saklar hidup
  }
  else if(aksi == '0'){
    digitalWrite(pin, LOW); //saklar mati
  }
  
}
