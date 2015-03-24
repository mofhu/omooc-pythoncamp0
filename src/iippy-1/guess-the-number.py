# Author Frank Hu
# Guess the Number!

import math
import random
import simplegui

def new_game_setter(max):
    global secret_number
    global attempts
    secret_number = random.randrange(1, int(max))
    attempts = int(math.ceil(math.log(max, 2)))
    if max:
        print 'New game begins! Range is [0, %d).'%(int(max))
    # print 'setting attempts', attempts

#inialize global before first enter
new_game_setter(100)        

def new_game():
    new_game_setter(range)

def new_game_100():
    global range 
    range = 100
    new_game_setter(range)

def new_game_1000():
    global range 
    range = 1000
    new_game_setter(range)

def enter(guess_input):	
    global attempts
    global range
    guess = int(guess_input) # better robustness needed
    # print 'secret number', secret_number # only for debugging

    attempts -=1
    print 'Guess number is', guess
    if secret_number == guess:
        print 'Correct!'
        new_game()
    elif secret_number > guess:
        print 'Lower!'
        print 'Ramaining attempts is', attempts
    else:
        print 'Higher!'	    
        print 'Ramaining attempts is', attempts
    if attempts == 0:
        print 'Game over! The secret number is', secret_number, 'better luck next time:)'
        new_game()

# create frame
frame = simplegui.create_frame("Guess the number, 1 to 100",300,300)

# register event handlers and create control elements
frame.add_button("New Game", new_game, 100)
frame.add_button("Range [0,100)", new_game_100, 100)
frame.add_button("Range [0,1000)", new_game_1000, 100)
frame.add_input("Enter", enter, 100)

# get frame rolling
frame.start()