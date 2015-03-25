import os
import time

def child():
	print 'Lapsi', os.getpid( )
	while(1):
		time.sleep(1)
		print "bum"
	os._exit(0)

def child2():
	print 'Lops', os.getpid( )
	while(1):
		time.sleep(2)
		print "tss"
	os._exit(0)

def parent():
	while True:
		newpid = os.fork()
		if newpid == 0:
			child()
			child2()
		else:
			pids = (os.getpid(), newpid)
		if raw_input( ) == 'q': break

parent()
