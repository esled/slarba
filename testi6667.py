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
	window.resize(600,450)
	window.connect('destroy',gtk.main_quit)	

	# horizontal layout for widgets inside main window
	hbox = gtk.HBox()
	window.add(hbox)
	
	hbox2 = gtk.HBox()
	window.add(hbox2)

	# label replicating the spin button value with formatting string
	label = gtk.Label()
	label.set_name('spin_value__label')
	label.set_markup('<b>%d</b>')
	hbox.add(label)
	 
	label2 = gtk.Label(gtk.Adjustment(0,0,500,1,5,0)
	label2.set_angle(45)
	label2.set_name('testi')
	label2.set_markup(str(kissa))
	hbox2.add(label2)

	# spin button
	spinbutton = gtk.SpinButton(gtk.Adjustment(0,0,100,1,5,0))
	spinbutton.set_name('spin_value__spinbutton')
	hbox.add(spinbutton)

	# show all widgets
	window.show_all()


	# the variable holding the spin button value
	self.spin_value = 0

 #### MAIN

example = Example()				 # instantiate the application
example.avc_init()				  # connect widgets with variables
gtk.main()						# run GTK event loop until quit
#### END