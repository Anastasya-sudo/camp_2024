int led = 13; //переменная с номером пина светодиода

int ldr = 0; //и фоторезистора

void setup() //процедура setup

{

pinMode(led, OUTPUT); //указываем, что светодиод - выход

}

void loop() //процедура loop

{

if (analogRead(ldr) < 800) digitalWrite(led, HIGH);

//если показатель освещенности меньше 800, включаем светодиод

else digitalWrite(led, LOW); //иначе выключаем

}



