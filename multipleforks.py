import os, time, sys, Adafruit_DHT
from multiprocessing import Value, Array
from subprocess import call

NUM_PROCESSES = 7

kissa = Value('d', 1.0)
kissat= Array('i', range(10))

def ProcessSelectFunction(process):
	if process == 0:
		time.sleep(0.06)
		gps()
	elif process == 1:
		time.sleep(0.05)
		rtc()
	elif process == 2:
		time.sleep(0.04)
		can()
	elif process == 3:
		time.sleep(0.03)
                i2c()
        elif process == 4:
		time.sleep(0.02)
                display()
	elif process == 5:
		time.sleep(0.01)
		anturit()
	elif process == 6:
		DHT()
def gps():
	print "gps paalla\n"
def rtc():
	print "RTC paalla\n"
	print "Kello on %s\n" % time.time()
def can():
	print "CAN bus paalla\n"
def i2c():
	print "I2C paalla\n"
def display():
        print "Display prosessi paalla\n"
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

