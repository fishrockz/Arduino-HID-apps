#include "USBLibaryHID.h"
#include <Arduino.h>

//volatile uint16_t interrupt_count[100]={0};

void willslibUSBLib_::Func(void)
{
	if (!flag==1){
		Serial.print("\nend point Func! dong dong dong\n");
		
		
	}
	uint8_t data[64]={0};
	
	if (USBDevice.getState(data,64)){
		int len=0;
		while(len<=64)
		{
				
			Serial.write(data[len]);
			len++;
		}


		int input = *VarWatch ;
		data[0] = (input & 0xff00) >> 8;
		data[1] = input & 0x00ff;
		//data[0]=sensorValue;
		USBDevice.setState(data,64);
		//Serial.write(55);
		willslibUSBLib.reset();
		
	}
	
	//flag=1;
}
void willslibUSBLib_::reset(void)
{
	flag=0;
}

void willslibUSBLib_::setwatch(int* data){

	VarWatch = data;

}

willslibUSBLib_ willslibUSBLib;
