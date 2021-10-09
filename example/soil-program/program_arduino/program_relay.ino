// membuat fungsi program relay untuk proteus
void relay_proteus(int pin){
  int perintah = Serial.read();
  
  if(perintah == '1'){ // Jika perintah relay hidup
    digitalWrite(pin, HIGH);
  }
  else if(perintah == '0'){
    digitalWrite(pin, LOW);
  }
}

// Membuat fungsi program relay untuk bord arduino asli
void relay_bord(int pin){
  int perintah = Serial.read();
  
  if(perintah == '1'){ // Jika perintah relay hidup
    digitalWrite(pin, LOW);
  }
  
  else(perintah == '0'){ // Jika perintah relay mati
    digitalWrite(pin, HIGH);
  }
}
