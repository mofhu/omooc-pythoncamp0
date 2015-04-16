# Author Frank Hu
# Hacker and Painter, watercolor version
# V0.2, 20150416

import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import re

# initalize globals
# 3 lists for storing different parameters, using index to sync.
# need to use the same index[] when cross-talking in different lists
# object-oriented skill maybe a good idea for more complicated work.
WIDTH = 600
HEIGHT = 600
color_in_use = 'Black'
shape_in_use = 'Circle'
size_in_use = 10
drawing_list = []
temp_drawing_list = []
interval = 400
time = 0 # for count ticking
timer = 0 
UI_protect = False 

class Drawing:
    # class for a single draw action
    # note: type of painter maybe added in later version.
    def __init__(self, color, position, shape, size):
        self.color = color
        self.position = position
        self.shape = shape
        self.size = size
    def __str__(self): # print for debugging
        return self.color, self.position, self.shape, self.size

class Pixel:
    # class for a single pixel, storing its color and position
    # may be defined as a single pixel Drawing.
    def __init__(self, color, position):
        self.color = color
        self.position = position

def paint(canvas): # main print function
    # display color and shape in use, in canvas
    # as it is not supported to print on label
    for i in drawing_list:
        canvas.draw_circle(i.position, i.size, 1, i.color, i.color)
    '''i = 0
    while i < len(pos_list):
        if shape_list[i] == 'Circle': # first use "=" instead, a "classic" error
            canvas.draw_circle(pos_list[i], 20, 2, color_list[i], color_list[i])
        elif shape_list[i] == 'Triangle':
            canvas.draw_polygon([(pos_list[i][0],pos_list[i][1] + 20),
                                (pos_list[i][0] + 10,pos_list[i][1] - 10),
                                (pos_list[i][0] - 10,pos_list[i][1] - 10)],
                                2, color_list[i])
        else: # i.e.: shape_list == "square" 
            canvas.draw_polygon([(pos_list[i][0] - 15,pos_list[i][1] + 15),
                                (pos_list[i][0] + 15,pos_list[i][1] + 15),
                                (pos_list[i][0] + 15,pos_list[i][1] - 15),
                                (pos_list[i][0] - 15,pos_list[i][1] - 15)],
                                2, color_list[i])
        i += 1'''
    # protect from input when playing
    if UI_protect == True:
    	    canvas.draw_text('Playing, not able to draw now.',
    	    	            (20,20), 14, 'Black')
    	    return
    canvas.draw_text('Color in use: %s' % (color_in_use), 
                     (20, 20), 14, 'Black') 
    canvas.draw_text('Shape in use: %s' % (shape_in_use), 
                     (20, 40), 14, 'Black') 
    canvas.draw_text('Play interval in use: %s' % (interval),
                     (20, 60), 14, 'Black') 


def append_drawing(mouse_click): # catch mouse click when not playing
    if UI_protect == False: #i.e. not protecting
        print mouse_click, color_in_use, shape_in_use, size_in_use
        single_drawing = Drawing(color_in_use, mouse_click, shape_in_use, size_in_use)
        drawing_list.append(single_drawing)
    
def color_setter(color_input): # input color
    global color_in_use
    # regular expression for robustness. Never be afraid of bad guys now, haha:) 
    # return wrong in console
    # the expression is found online. No time to learn it this week...
    valid_color_list = ['aqua', 'black', 'blue', 'fuchsia', 'gray',\
                'green', 'lime', 'maroon', 'navy', 'olive', 'orange',\
                'purple', 'red', 'silver', 'teal', 'white', 'yellow']
    # match rgb #xxx format
    if re.match("^#[0-9a-fA-F]{3}$", color_input, ): 
        color_in_use = color_input
    # match reb #xxxxxx format
    elif re.match("^#[0-9a-fA-F]{6}$", color_input, ): 
    	color_in_use = color_input
    else:
    	# match color list
    	for i in valid_color_list:
    		if color_input.lower() == i:
    			color_in_use = i
    			return
    	# wrong input
        print 'Wrong color input! Please input the right color format!'    

# set shapes
def shape_setter_circle():
    global shape_in_use
    shape_in_use = 'Circle'

def shape_setter_triangle():
    global shape_in_use
    shape_in_use = 'Triangle'

def shape_setter_square():
    global shape_in_use
    shape_in_use = 'Square'

def play():
    # 1: process lists to temp place
    global drawing_list
    global temp_drawing_list
    global timer
    global UI_protect
    temp_drawing_list = drawing_list
    # 2: clear list
    drawing_list = []
    # 3: remake list with delay
    print interval
    timer = simplegui.create_timer(interval, tick)
    timer.start()
    UI_protect = True

def tick():
    # playing with interval, as canvas is always drawing
    # appending new steps with interval to play
    global time 
    global timer
    global UI_protect
    if time < len(temp_drawing_list):
        drawing_list.append(temp_drawing_list[time])
        time += 1
        print time
    else:
        timer.stop()
        UI_protect = False
        time = 0
        print "Play finished!"

def change_interval(interval_input): # change interval
    global interval
    # regular expression for robustness. Never be afraid of bad guys now, haha:) 
    # return wrong in console
    if re.match("^[0-9]*[1-9][0-9]*$", interval_input, ): 
        interval = int(interval_input)
    else:
        print 'Wrong interval input! Please input a number!'
    print interval

# create frame
frame = simplegui.create_frame('Canvas', WIDTH, HEIGHT)
frame.set_canvas_background('White')
frame.set_draw_handler(paint)

# set event handler
frame.set_mouseclick_handler(append_drawing) # get click position
# use a input box to get color
# rewrite it in a label...
frame.add_input('Color: valid input is aqua, black, blue, fuchsia, gray,\
                green, lime, maroon, navy, olive, orange, purple, red,\
                silver, teal, white, yellow. \nAnd rgb format #xxx or \
                #xxxxxx (x=0-9A-F),\n \
                Bad input information is shown in console.',
                color_setter, 150) 
# 3 buttoms for setting shape
frame.add_button('Circle', shape_setter_circle, 150) 
frame.add_button('Square', shape_setter_square, 150)
frame.add_button('Triangle', shape_setter_triangle, 150)
# button to play whole progress
frame.add_button('Play', play, 150)
frame.add_input('Play interval', change_interval, 150)

#start frame
frame.start()