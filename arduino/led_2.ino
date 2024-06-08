const int led = 9;  // Константа - номер контакта светодиода

void setup(){
  pinMode(led, OUTPUT); // Конфигурируем контакт светодиода как выход
  digitalWrite(led, HIGH);  // Устанавливаем значение HIGH на выходе
}

void loop(){
  digitalWrite(led, HIGH);
  delay(1000);
  digitalWrite(led, LOW);
  delay(1000); 
}
