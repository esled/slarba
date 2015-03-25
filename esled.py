import os, time, sys, Adafruit_DHT
from multiprocessing import Value, Array
from subprocess import call

NUM_PROCESSES = 7

GPS_Data = Value('d',0.0)
RTC_Data = Value('s',"kissa")
CAN_Data = Value('s',"Koira")
I2C_Data = Value('d',1.0)

kissa = Value('d', 1.0)
kissat= Array('i', range(10))

def ProcessSelectFunction(process):
	if process == 0:
		gps()
	elif process == 1:
		rtc()
	elif process == 2:
		can()
	elif process == 3:
		i2c()
	elif process == 4:
		display()
	elif process == 5:
		anturit()
	elif process == 6:
		DHT()
		
def gps():
	GPS_Data.Value = 1.0
def rtc():
	RTC_Data.Value = time.time()
def can():
	CAN_Data.Value = "Kissa"
def i2c():
	I2C.Data.Value = 0
def display():
	
def anturit():
	contents = open("/sys/bus/w1/devices/28-00000696b200/w1_slave", "r").read().split()
	contents2 = contents[-1].split("=")
	contents3 = int(contents2[-1])
	print "Dallas 1-wire anturit:"
	print "Temp sensor 1. s/n 28-00000696b200"
	print "Arvo : {0:0.1f}*C\n".format(contents3/1000.)
	
def DHT():
	humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, "17")
	if humidity is not None and temperature is not None:
		print "DHT anturi 1"
		print 'Temp={0:0.1f}*C\nHumidity={1:0.1f}%\n'.format(temperature, humidity)
	else:
		print 'Arvojen lukeminen anturilta DHT22 portissa GPIO17 epaonnistui!\n'



while 1:	
	time.sleep(1)
	os.system('clear')
	children = []
	
	print "GPS koordinaatti : %d" % GPS_Data.Value
	print "RTC aika: %s" % RTC_Data.Value
	print "CAN tila: %s" % CAN_Data.Value
	print "I2C tila: %d" % I2C_Data.Value
	
	start_time = time.time()
	for process in range(NUM_PROCESSES):
		pid = os.fork()
		if pid:
			children.append(pid)
		else:
			ProcessSelectFunction(process)
			os._exit(0)

	for i, child in enumerate(children):
		os.waitpid(child, 0)

	print time.time() - start_time

