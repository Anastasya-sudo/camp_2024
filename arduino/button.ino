const int led = 9;  // контакт 9 для подключения светодиода
const int button = 2;

void setup(){
  pinMode(led, OUTPUT); // конфигурируем контакт светодиода как выход
  pinMode(button, INPUT); //  конфигурировать контакт кнопки как вход
}

void loop(){
  if (digitalRead(button) == LOW) // считываем значение сигнала на входе и делаем проверку
  {
    digitalWrite(led, LOW);
  }
  else
  {
    digitalWrite(led, HIGH);
  }
}
