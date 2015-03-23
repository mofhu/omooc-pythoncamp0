# Author Frank Hu
# Guess the Number!

import random
import simplegui

def new_game():
	global secret_number
	secret_number = random.randrange(1, 100)

def enter(guess_input):	
	guess = int(guess_input)
	if secret_number == guess:
		print 'Correct!'
	elif secret_number > guess:
		print 'Lower!'
	else:
		print 'Higher!'

# create frame
frame = simplegui.create_frame("Guess the number, 1 to 100",300,300)

# register event handlers and create control elements
frame.add_button("New Game", new_game, 100)
frame.add_input("Enter", enter, 100)

# get frame rolling
frame.start()

#inialize global before first enter
new_game()