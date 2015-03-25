import os
import time

def child():
	print 'Lapsi', os.getpid( )
	while(1):
		time.sleep(1)
		print time.asctime()
	os._exit(0)

def parent():
	while True:
		newpid = os.fork()
		if newpid == 0:
			child()
		else:
			pids = (os.getpid(), newpid)
			print "mami: %d, Laps: %d" % pids
			time.sleep(3)
			print 'arg'
		if raw_input( ) == 'q': break

parent()
