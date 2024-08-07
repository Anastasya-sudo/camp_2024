int Pin_VRX = A0; //пин оси x джойстика

int Pin_VRY = A1; //пин оси y джойстика

int Button_Pin = 2; //пин кнопки джойстика

void setup() {

Serial.begin(9600); //устанавливаем скорость обмена данными 9600 бод

pinMode(Button_Pin, INPUT); //переводим пин кнопки в режим ввода данных

digitalWrite(Button_Pin, HIGH);

}

void loop() {

int X = analogRead(Pin_VRX); //переменная X - значения по оси x

int Y = analogRead(Pin_VRY); //переменная Y - значения по оси y

int B = digitalRead(Button_Pin);//переменная B считывает значения с кнопки

//выводим переменную X

Serial.print("X = ");

Serial.println(X);

//выводим переменную Y

Serial.print("Y = ");

Serial.println(Y);

//проверка состояния кнопки

if(B == 1) { //если кнопка не нажата

Serial.println("Button not click"); //выводим "Button not click"

}else{ //иначе

Serial.println("Button click"); //выводим "Button click"

}

delay(1000); //задержка 1 секунда

}