import microstacknode.gps.l80gps, time

gps = microstacknode.gps.l80gps.L80GPS()

database = open('gps_database', 'a')
last_data = open('gps_data', 'w')
while 1:
	data = gps.gpgga
	gps_data = str(data['utc']) + ";" + str(data['longitude']) + ";" + str(data['latitude']) + ";\n"
	database.write(gps_data)
	last_data.write(gps_data)
	time.sleep(0.49)
	


