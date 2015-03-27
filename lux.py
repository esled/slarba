import TSL2561, time

tsl=TSL2561()
while 1:
	print tsl.readLux()
	time.sleep(0.1)
