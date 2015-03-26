import microstacknode.gps.l80gps, time

gps = microstacknode.gps.l80gps.L80GPS()

file = open('gps_data', 'a')
while 1:	
	while 1:
		gps_data = str(gps.gpgga['utc']) + ";" + str(gps.gpgga['longitude']) + ";" + str(gps.gpgga['latitude']) + ";\n"
		file.write(gps_data)
		time.sleep(0.49)

time.sleep(5)	


