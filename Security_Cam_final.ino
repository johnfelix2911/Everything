#include "BluetoothSerial.h"     //Include headerfile for Bluetooth serial

BluetoothSerial Security_Cam;    //Create a bluetoothserial object named 'Security_Cam'

int PIR_pin = 13;           //Initiallize pin 13 to connect to PR sensor output
int PIR_pin_status = 0;     //A variable to store the current status of PIR pin [HIGH=1 and LOW=0]

void setup() {
  Serial.begin(9600);      //Begin serial communication
  pinMode(PIR_pin, INPUT);  //Set PIR pin to accept INPUT
  Security_Cam.begin("Security_Cam");  //Bluetooth device name
}

void loop() {
  if (PIR_pin_status == 0 && digitalRead(PIR_pin) == 1) {   
    //Checks if initially the PIR pin was LOW and now it is HIGH
    Security_Cam.println("Motion detected");   //Print "Motion detected"
    PIR_pin_status = 1;    //Toggles (changes) the value of PIR_pin_status variable
  } else if (PIR_pin_status == 1 && digitalRead(PIR_pin) == 0) {
    //Checks if initially the PIR pin was HIGH and now it is now
    Security_Cam.println("No motion");      //Print "No motion"
    PIR_pin_status = 0;   //Toggles (changes) the value of PIR_pin_status variable
  }
  delay(20);     //We add a delay to avoid overwhelming the esp32 with data
}
