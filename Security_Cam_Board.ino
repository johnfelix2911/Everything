#include "BluetoothSerial.h"

BluetoothSerial Security_Cam;

int PIR_pin = 3;
int PIR_pin_status = 0;

void setup() {
 Serial.begin(9600);
 pinMode(PIR_pin, INPUT);
 Security_Cam.begin("Security_Cam"); //Bluetooth device name
}

void loop() {
if (PIR_pin_status==0 && digitalRead(PIR_pin)==1){
  Security_Cam.println("Motion detected");
  PIR_pin_status=1;
}
else if (PIR_pin_status==1 && digitalRead(PIR_pin)==0){
  Security_Cam.println("No motion");
  PIR_pin_status=0;
}
 delay(20);
}
