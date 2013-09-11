import usb.core,sys,time
import usb.util
import usb
#help(usb.core) 
busses = usb.busses()
for bus in busses:
	devices = bus.devices
	for dev in devices:
		try:
			_name = usb.util.get_string(dev.dev,256,2)
			print _name
		except:
			pass

printers = usb.core.find(find_all=True)#, bDeviceClass=7)
foundit=0
for dev in printers:
	print 'dev',dev
	#print 'dev',dev.idVendor,dev.idProduct,usb.util.get_string(dev.dev, 256, 2)
	print 'ard','0x2341','0x8036' 
	print int('0x2341', 16),int('0x8036', 16)
	print type(dev.idVendor)
	print dev.idVendor==int('0x2341', 16)
	
	for cfg in dev:
	    sys.stdout.write(str(cfg.bConfigurationValue) + '\n')
	    for intf in cfg:
		sys.stdout.write('\t' + \
		                 str(intf.bInterfaceNumber) + \
		                 ',' + \
		                 str(intf.bAlternateSetting) + \
		                 ',' + \
		                 str(intf.bInterfaceClass) + \
		                 
		                 '\n')
		for ep in intf:
		    sys.stdout.write('\t\t' + \
		                     str(ep.bEndpointAddress) + \
		                     '\n')
	if   dev.idVendor==int('0x2341', 16):
		foundit=1
		break
if not foundit: exit()
print dir(dev)	
DetK=1
if DetK: dev.detach_kernel_driver(intf)	

#dev.set_configuration()    

#The first, third and fourth parameters are equal for both methods, they are the endpoint address, interface number and timeout, respectivelly. The second parameter is the data payload (write) or the number of bytes to read (read). The return of the read function is an instance of the array object or the number of bytes written for the write method.
if 1:
	msg = 'Hello every one this is very crasy\n'
	msg = '\nHello every one this is very crasy\n'
	#msg=chr(5)*4
	#msg = 'tttttttttttttttt'
	#for x in range(10):
	
	try:
		for ii in range(10):
			print "dev.write(5, msg, 2, 3000)",dev.write(5, msg, 2, 3000)

			try:
				dat= dev.read(132, 64, 2, 100)
				print 'data',dat
				#if data==255:
				if  len(dat) == 64:
					print 'number:',dat[1]*255+dat[2]
			except:
				print 'failed to read packet'
			time.sleep(1)
	finally:

		usb.util.dispose_resources(dev)
		#time.sleep(1)
		if DetK:dev.attach_kernel_driver(intf)
	#for x in range(20):
	#	print dev.read(132, 9, 2, 1500)

	#time.sleep(1)
	#usb.util.dispose_resources(dev)
	#dev.attach_kernel_driver(intf)
else:
	try:
		while 1:
			print 'dev.read', dev.read(132, 15, 2, 2000)
			#time.sleep(0.5)
	finally:

		usb.util.dispose_resources(dev)
		if DetK:dev.attach_kernel_driver(intf)
#attach_kernel_driver()
















