import os, time
from multiprocessing import Value, Array

NUM_PROCESSES = 7

kissa = Value('d', 1.0)
kissat= Array('i', range(10))

def ProcessSelectFunction(process):
	if process == 0:
		gps()
	if process == 1:
		print "rosessi %s" % process
	else:
		print process
		x = 1
		print kissa.value
		for n in xrange(10000000):
			x += 1
		kissa.value = time.time() - start_time
		print kissa.value
def gps():
	print "gps paalla"
	print kissat[:]
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

