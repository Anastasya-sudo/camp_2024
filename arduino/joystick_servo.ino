#define pinX A1       // ось X джойстика

#include <Servo.h> // подключаем библиотеку для серво
Servo servo1;           // объявляем объект servo1

void setup() {
   pinMode(pinX, INPUT); // указываем пин для джойстика

   servo1.attach(10);            // указываем пин для микро серво
}
 
void loop() {
   int X = analogRead(pinX);      // считываем значение оси X

   X = map(X, 0, 1023, 0, 180); // переводим значение X в новый диапазон
  
   servo1.write(X);                      // поворачиваем серво от джойстика
}