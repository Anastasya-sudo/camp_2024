#include <NewPing.h>
#include <Wire.h>
#include <LiquidCrystal_I2C.h>      // подключаем библиотеку. 

#define PIN_TRIG 12
#define PIN_ECHO 11
#define PIN_LED 13
#define PIN_LED1 9

LiquidCrystal_I2C lcd(0x27,16,2);   // Устанавливаем дисплей (Первый параметр — адрес,
                                    // найденный сканером, 2-й количество символов в строке
                                    // 3-й количество строк.

#define MAX_DISTANCE 200 // Константа для определения максимального расстояния, которое мы будем считать корректным.

// Создаем объект, методами которого будем затем пользоваться для получения расстояния.
// В качестве параметров передаем номера пинов, к которым подключены выходы ECHO и TRIG датчика

NewPing sonar(PIN_TRIG, PIN_ECHO, MAX_DISTANCE);

void setup() {
  // Инициализируем взаимодействие по последовательному порту на скорости 9600
  Serial.begin(9600);
  pinMode(PIN_LED, OUTPUT);
  pinMode(PIN_LED1, OUTPUT);

  lcd.init();                    
  lcd.backlight();// Включаем подсветку дисплея
}

void loop() {

  // Стартовая задержка, необходимая для корректной работы.
  delay(50);

  // Получаем значение от датчика расстояния и сохраняем его в переменную
  unsigned int distance = sonar.ping_cm();

  // Печатаем расстояние в мониторе порта
  Serial.print(distance);
  Serial.println("см");

  if (distance <= 10){
    digitalWrite(PIN_LED, HIGH);
    digitalWrite(PIN_LED1, HIGH);

    lcd.print("Hello, world!");  // Выводим фразу

  }else{
    digitalWrite(PIN_LED, LOW);
    digitalWrite(PIN_LED1, LOW);

    lcd.print("             ");  // Удаляем фразу
  }


}



