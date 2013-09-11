#include <Arduino.h>


#include "USBLibaryHID.h"

uint8_t data[64]={0};
int len = 64;

int sensorPin = A0;    // select the input pin for the potentiometer
int ledPin = 13;      // select the pin for the LED
int sensorValue = 0;  // variable to store the value coming from the sensor



void quicfunc() {
	willslibUSBLib.Func();
}

void setup()
{
	//pinMode(13, OUTPUT);

        USBDevice.attach();
        pinMode(ledPin, OUTPUT);  
        USBDevice.setFunc(&quicfunc);
	willslibUSBLib.setwatch(&sensorValue);

}


void loop()
{
	


		delay(100);

		sensorValue = analogRead(sensorPin);
		
		
		
		
		

}
