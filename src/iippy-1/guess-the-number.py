# Author Frank Hu
# Guess the Number!
# V2.0
# Fix #1: output by message box, not only in console
# Fix #2: robust inputbox (blank input finished, character input remains a problem)

import math
import random
import simplegui

def new_game_setter(max):
    global secret_number
    global attempts
    global message 
    #global gametype
    secret_number = random.randrange(1, int(max))
    attempts = int(math.ceil(math.log(max, 2)))
    if max:
        print 'New game begins! Range is [0, %d).'%(int(max))
        #game_type = 'Range is [0, %d).'%(int(max))
        #print game_type
    # print 'setting attempts', attempts
    
#inialize global before first enter
new_game_setter(100)
message = 'New game begins!'
global range 
range = 100
    
#feedback message
def show_message(canvas):
    canvas.draw_text('%s'%(message), [0,40], 20, "Red")
    
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
    global message
    global game_type
    if guess_input: # to see if the imput is NULL
        guess = int(guess_input) 
    else: 
        print 'No input, please input a number between 0 and %d!'%(range)
        message = 'No input, please input a number between 0 and %d!'%(range)
        return
    # print 'secret number', secret_number # only for debugging

    attempts -=1
    print 'Guess number is', guess
    if secret_number == guess:
        print 'Correct!'
        message = 'Correct!'
        new_game()
    elif secret_number > guess:
        print 'Lower!'
        print 'Ramaining attempts is', attempts
        message = 'Lower! Ramaining attempts is %d'%(attempts)
    else:
        print 'Higher!'     
        print 'Ramaining attempts is', attempts
        message = 'Higher! Ramaining attempts is %d'%(attempts)
    if attempts == 0:
        print 'Game over! The secret number is', secret_number, 'better luck next time:)'
        message = 'Game over! The secret number is %d better luck next time:)'%(attempts)
        new_game()

# create frame
frame = simplegui.create_frame("Guess the number, by Frank Hu",600,300)

# register event handlers and create control elements
frame.add_button("New Game", new_game, 100)
frame.add_button("Range [0,100)", new_game_100, 100)
frame.add_button("Range [0,1000)", new_game_1000, 100)
frame.add_input("Enter", enter, 100)
frame.set_draw_handler(show_message)

# get frame rolling
frame.start()