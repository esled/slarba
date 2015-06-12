import gtk						# gimp tool kit bindings

from avc import *				   # AVC


class Example(AVC):
   """
   A spin button whose value is replicated into a label
   """

   def __init__(self):

	## create GUI

	kissa = 200
	# main window
	window = gtk.Window()
	window.set_title('Sporon Spermometer')
	window.resize(600,500)
	window.connect('destroy',gtk.main_quit)	

	# horizontal layout for widgets inside main window
	hbox = gtk.HBox()
	window.add(hbox)
	col1 = gtk.VBox()
	col2 = gtk.VBox()
	hbox.add(col1)
	hbox.add(col2)
	

	# label replicating the spin button value with formatting string
	label = gtk.Label()
	label.set_name('testi2')
	label.set_markup('<span size="20000"><b>Kellonaika</b></span>\n<span size="20000"><b>Koordit</b></span>\n<span size="20000"><b>CANintila</b></span>\n<span size="40000"><b>KISSA</b></span>\n<i><span size="20000"><b>KISSA</b></span></i>\n<span size="20000"><b>KISSA3</b></span>')
	col2.add(label)
	 
	label2 = gtk.Label()
	#label2.set_angle(190)
	label2.set_name('testi')
	label2.set_markup('<span size="20000">Kello:</span>\n<span size="20000">GPS:</span>\n<span size="20000">CAN:</span>\n<span size="20000">I2C:</span>\n<span size="20000">TEMP:</span>\n<span size="20000">HUM:</span>')
	col1.add(label2)


	# show all widgets
	window.show_all()


	# the variable holding the spin button value
	self.spin_value = 0

 #### MAIN

example = Example()				 # instantiate the application
example.avc_init()				  # connect widgets with variables
gtk.main()						# run GTK event loop until quit
#### END
