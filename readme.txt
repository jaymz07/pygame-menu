Simple menu class for pygame library. Makes for an extremely easy to use right click menu.

-----------Usage-------------
Put the menu.py file in same directory as program needing a menu. The program can then use the library as follows
 -Import the Menu class
 -Set up menu properties
 -Assign functions
 -Pass user input to menu
 -Draw menu to screen

A working example is provided in menuTest.py
The example is supposed to look similar to other examples in the pygame documentation.

----------Example Implementation------------------

	#Import the library
	from menu import Menu

	.
	.
	.

	#Define the menu entries
	menuEntries = ['Do a Thing', 'Do another thing', 'Do nothing']

	#Create the menu
	inputMenu = Menu( [300,300], menuEntries, rightClick = True)

	#Assign some functions
	inputMenu.assignFunction(0,f1)
	inputMenu.assignFunction(1,f2)

	.
	.
	.

	(inside of main program loop)
		.
		.
		.
		#Process User input
		for event in pygame.event.get():
			#Pass input events to menu
			inputMenu.processMouseInput(event)	
			.
			.
			.
		.
		.
		.
		#Draw the menu on the screen
		inputMenu.draw(screen)
		.
		.
		.
		
