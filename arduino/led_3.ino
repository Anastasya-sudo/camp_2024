const int led = 9;  // Константа - номер контакта светодиода

void setup(){
  pinMode(led, OUTPUT); // Конфигурируем контакт светодиода как выход
  digitalWrite(led, HIGH);  // Устанавливаем значение HIGH на выходе
}

void loop(){
  for (int i = 100; i <= 1000; i = i+100){
    digitalWrite(led, HIGH);
    delay(i);
    digitalWrite(led, LOW);
    delay(i); 
  }
}
