import os, time
from multiprocessing import Value, Array

NUM_PROCESSES = 7

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
	else:
		print process
		x = 1
	
		for n in xrange(100000):
			x += 1
		kissa.value = time.time() - start_time
		print kissa.value
def gps():
	print "gps paalla"
def rtc():
	print "rtc paalla"
def can():
	print "CAN bus paalla"
def i2c():
	print "I2C paalla"
def display():
        print "Display prosessi paalla"
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

