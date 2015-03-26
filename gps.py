import microstacknode.gps.l80gps, time

gps = microstacknode.gps.l80gps.L80GPS()

file = open('gps_data', 'a')
while 1:
	data = gps.gpgga
	gps_data = str(data['utc']) + ";" + str(data['longitude']) + ";" + str(data['latitude']) + ";\n"
	file.write(gps_data)
	time.sleep(0.49)
	


