# -*- coding: utf-8 -*-
# Author Frank Hu
# Hacker and Painter, watercolor version
# V3.0 mini loader, 20150422

import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import watercolor_packet as watercolor
import random

# initalize globals
WIDTH = 300
HEIGHT = 300
SIZE = 10
size_in_use = SIZE
color_in_use = 'rgb(0,255,255)'

def append_drawing(mouse_click): 
	# catch mouse click and draw
	# Drawing means a single circle in this watercolor painter
	# it has 3 parameters: color, position and size(radius).
	# IMPORTANT: do not recommand size more than 20. 
	# as it will be too slow for refreshing many dots at 60 Hz
    print mouse_click, color_in_use, size_in_use # for debugging
    single_drawing = watercolor.Drawing(color_in_use, mouse_click, size_in_use)
    single_drawing.draw_pixel()

def color_setter(color_input): 
	# use a color setter to input color
	# IMPORTANT: color input must be in r,g,b format.
	# e.g. 0,255,255
    global color_in_use
    color_in_use = 'rgb(' + str(color_input) + ')' 
    watercolor.color_in_use = color_in_use

def random_color():
    global color_in_use
    random_color_tuple = (random.randrange(0,255),
                          random.randrange(0,255),
                          random.randrange(0,255))
    color_in_use = 'rgb' + str(random_color_tuple)
    watercolor.color_in_use = color_in_use

# create frame
frame = simplegui.create_frame('Hacker and painter, watercolor version', WIDTH, HEIGHT)
frame.set_canvas_background('White')
frame.set_draw_handler(watercolor.paint)

# set event handler
frame.set_mouseclick_handler(append_drawing) # get click position
# use a input box to get color
# rewrite it in a label...
frame.add_input('Color: valid input is r,g,b. e.g.: 0,255,255',
                color_setter, 150) 
# buttoms for setting shape and color
frame.add_button('Random color', random_color, 150)

#start frame
frame.start()