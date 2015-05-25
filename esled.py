import os, time, sys, sht21#, Adafruit_DHT
from multiprocessing import Value, Array
from subprocess import call

with sht21.SHT21(1) as sht21:
	print "T: %s"%sht21.read_temperature()
	print "H: %s"%sht21.read_humidity()

NUM_PROCESSES = 7 #JOS DHT22 -> 8

#GPS muuttujat
#GPS_Data = Value('d',0.0)
Longitude = Value('d',0.0)
Latitude = Value('d',0.0)


RTC_Data = Array('c',"kissa                          ")
I2C_Data = Value('d',1.0)
D1W_1 = Value('d',0.0)
DHT_1_T = Value('d',0.0)
DHT_1_H = Value('d',0.0)
DHT_1_W = Value('i',5)
SHT21_T = Value('d',0.0)
SHT21_H = Value('d',0.0)

CAN_Data = Array('c',"Off")

kissa = Value('d', 1.0)
kissat= Array('i', range(10))

flag = Value('i', 0)
child_flag = Value('i',0)

def ProcessSelectFunction(process):
	if process == 0:
		screen()
	elif process == 1:
		gps()
	elif process == 2:
		rtc()
	elif process == 3:
		can()
	elif process == 4:
		i2c()
	elif process == 5:
		display()
	elif process == 6:
		anturit()
	elif process == 7:
		DHT()
		
def screen():
	clk = 0
	while child_flag.value == 1:
		os.system('clear')
		print "GPS data :\nLongitude= {0:0.5f}\nLatitude = {1:0.5f}\n".format(Longitude.value, Latitude.value) #GPS_Data.value
		print "RTC aika: %s" % RTC_Data.value
		print "CAN tila: %s" % CAN_Data.value
		print "I2C tila: %d" % I2C_Data.value
		print " "
		print "Dallas 1-wire anturit:"
		print "Temp sensor 1. s/n 28-00000696b200"
		print u"Arvo : {0:0.1f}\u00b0C\n".format(D1W_1.value)
		print " "
		print "DHT anturi 1"
		print u'Temp={0:0.1f}\u00b0C\nHumidity={1:0.1f}%\n'.format(DHT_1_T.value, DHT_1_H.value)

		print "SHT Anturi"
		print u'Temp: {0:0.1f}\u00b0C'.format(SHT21_T.value)
		print "Hum : {0:0.1f}%".format(SHT21_H.value)
		while flag.value == clk:
			pass			
		clk = flag.value
	print "ERROR"



#def screen():
#	clk = 0
#	while child_flag.value == 1:
#		os.system('clear')
#		print "GPS data :\nLongitude= {0:0.5f}\nLatitude = {1:0.5f}\n".format(Longitude.value, Latitude.value) #GPS_Data.value
#		print "RTC aika: %s" % RTC_Data.value
#		print "CAN tila: %s" % CAN_Data.value
#		print "I2C tila: %d" % I2C_Data.value
#		print " "
#		print "Dallas 1-wire anturit:"
#		print "Temp sensor 1. s/n 28-00000696b200"
#		print u"Arvo : {0:0.1f}\u00b0C\n".format(D1W_1.value)
#		print " "
#		print "DHT anturi 1"
#		print u'Temp={0:0.1f}\u00b0C\nHumidity={1:0.1f}%\n'.format(DHT_1_T.value, DHT_1_H.value)
#
#		print "SHT Anturi"
#		print u'Temp: {0:0.1f}\u00b0C'.format(SHT21_T.value)
#		print "Hum : {0:0.1f}%".format(SHT21_H.value)
#		while flag.value == clk:
#			pass			
#		clk = flag.value
#	print "ERROR"
	


def gps():
	clk = 0
	while child_flag.value:
		#GPS_Data.value = 1.0
		GPS_Data = "74234.0;25.721899999999998;66.48173666666666"
		GPS_Data = GPS_Data.split(";")
		#print GPS_Data
		Longitude.value = float(GPS_Data[2])
		Latitude.value = float(GPS_Data[1])
		while flag.value == clk:
			pass
		clk = flag.value
		#print "hop"
		
def rtc():
	clk = 0
	while child_flag.value:
		RTC_Data.value = time.strftime("%d %b %Y %H:%M:%S")
		while flag.value == clk:
			pass
		clk = flag.value
		#print "hop"
		
def can():
	clk = 0
	while child_flag.value:
		CAN_Data.value = "On"
		while flag.value == clk:
			pass
		clk = flag.value
		#print "hop"
		
def i2c():
	clk = 0
	while child_flag.value:
		I2C_Data.value = 0
		while flag.value == clk:
			pass
		clk = flag.value
		#print "hop"
		
def display():
	clk = 0
	while child_flag.value:
		kissa.value = 2.1
		while flag.value == clk:
			pass
		clk = flag.value
		#print "hop"
		
def anturit():
	clk = 0
	while child_flag.value:
		contents = open("/sys/bus/w1/devices/28-00000696b200/w1_slave", "r").read().split()
		contents2 = contents[-1].split("=")
		contents3 = int(contents2[-1])
		D1W_1.value = contents3/1000.
		SHT21_T.value = sht21.read_temperature()
		SHT21_H.value = sht21.read_humidity()
		#SHT21_T.value = SHT21_T.value + 1
		#print SHT21_T.value
		while flag.value == clk:
			pass
		clk = flag.value
		#print "hop"
		
def DHT():
	clk = 0
	while child_flag.value:
	#	if DHT_1_W.value > 4:
	#		DHT_1_W.value = 0
	#		humidity, temperature = Adafruit_DHT.read(Adafruit_DHT.DHT22, "17")
	#		if humidity is not None and temperature is not None:
	#			DHT_1_T.value = temperature
	#			DHT_1_H.value = humidity
	#		else:
	#			print 'Arvojen lukeminen anturilta DHT22 portissa GPIO17 epaonnistui!\n'
	#	else:
	#		DHT_1_W.value = DHT_1_W.value + 1
		print 'Ei DTH-anturia'
		while flag.value == clk:
			pass
		clk = flag.value		
		#print "hop"
		
while 1:	
	children = []
	child_flag.value = 1
	for process in range(NUM_PROCESSES):
		pid = os.fork()
		if pid:
			children.append(pid)
		else:
			ProcessSelectFunction(process)
			os._exit(0)

	#for i, child in enumerate(children):
	#	os.waitpid(child, 0)
	start_time = time.time()
	while 1:
		print "fpm: %d" % (60/(time.time() - start_time))
		#print "\n\n\n"
		start_time = time.time()
		while (time.time() - start_time) < 0.1:
			pass
		if flag.value == 0:
			flag.value = 1
		else:
			flag.value = 0
	child_flag.value = 0
	start_time = time.time()
