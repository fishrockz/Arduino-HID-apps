#include <Arduino.h>
uint8_t data[64]={0};
int len = 64;

int sensorPin = A0;    // select the input pin for the potentiometer
int ledPin = 13;      // select the pin for the LED
int sensorValue = 0;  // variable to store the value coming from the sensor



void setup()
{
	//pinMode(13, OUTPUT);

        USBDevice.attach();
        pinMode(ledPin, OUTPUT);  
        


}


void loop()
{
	
	//while (1)
	//{
		delay(100);
		// Call Joystick.move
		//USBDevice.setState();
	
		if (USBDevice.getState(data,64)){
			len=0;
			while(len<=64)
			{
				
				Serial.write(data[len]);
				len++;
			}
			sensorValue = analogRead(sensorPin);
//			(n & 0xff00) >> 8
			data[0] = (sensorValue & 0xff00) >> 8;
			data[1] = sensorValue & 0x00ff;
			//data[0]=sensorValue;
			USBDevice.setState(data,64);
			//Serial.write(55);
		
		}
		//USBDevice.setState(data,64);
	//}
}
