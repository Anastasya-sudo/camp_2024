const int led = 9;  // Константа - номер контакта светодиода

void setup(){
  pinMode(led, OUTPUT); // Конфигурируем контакт светодиода как выход
  digitalWrite(led, HIGH);  // Устанавливаем значение HIGH на выходе
}

void loop(){
  for (int i = 0; i <= 256; i++){
    analogWrite(led, i);  // плавно уменьшаем/увеличиваем напряжение на 9м контакте
    delay(10); 
  }
  for (int i = 256; i >= 0; i--){
    analogWrite(led, i);
    delay(10); 
  }
}
