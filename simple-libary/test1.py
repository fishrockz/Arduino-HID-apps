import serial,time,sys
serAL = serial.Serial('/dev/ttyACM0', 9600)

#serUS = serial.Serial('/dev/ttyUSB0', 9600)
#serUS = serial.Serial('/dev/ttyUSB0', 115200)
#serUS = serial.Serial('/dev/ttyUSB0', 57600)

#ser=serUS
ser=serAL
line=''
t = time.time()
while 1:
	
	#serUS.write('cv')
	#print serAL.readline()
	#print serUS.read(),
	#print int(serAL.read(),2)
	ch=ser.read()
	#print ch,
	line+=ch
	sys.stdout.write(ch )
	if 10 == ord(ch): 
		#sys.stdout.write('\n')
		#print line,
		line=''
	sys.stdout.flush()
	if time.time()-t>5:
		ser.write('\n')
		t = time.time()
	#time.sleep(1)
	
