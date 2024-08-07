#include <Wire.h>
#include <LiquidCrystal_I2C.h>      // подключаем библиотеку. Она должна уже быть установлена
LiquidCrystal_I2C lcd(0x27,16,2);   // Устанавливаем дисплей (Первый параметр — адрес,
                                    // найденный сканером, 2-й количество символов в строке
                                    // 3-й количество строк.
void setup()
{
  lcd.init();                    
  lcd.backlight();// Включаем подсветку дисплея
  lcd.print("Hello, world!");  // Выводим стандартную фразу
  lcd.setCursor(0, 1);   // Устанавливаем курсор на вторую строку и нулевой символ.
  lcd.print("That is me.");      // «Это я»
}
 
void loop()
{
// Пустой цикл
}
