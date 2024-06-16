#include <Servo.h> // подключаем библиотеку для работы с сервоприводом
#include <NewPing.h>

#define PIN_TRIG 12
#define PIN_ECHO 11

#define MAX_DISTANCE 200

NewPing sonar(PIN_TRIG, PIN_ECHO, MAX_DISTANCE);
Servo servo1; // объявляем переменную servo типа "servo1"

void setup() {
  Serial.begin(9600);
  servo1.attach(10); // привязываем сервопривод к аналоговому выходу 11
  servo1.write(0); // ставим угол поворота под 0
}

void loop() {

  //Получаем значение от датчика расстояния и сохраняем его в переменную
  unsigned int distance = sonar.ping_cm();

  // Печатаем расстояние в мониторе порта
  Serial.print(distance);
  Serial.println("см");

  if (distance <= 10){
    servo1.write(90);
    //delay(2000);
  }else{
    servo1.write(0);
    //delay(2000);
  }
}