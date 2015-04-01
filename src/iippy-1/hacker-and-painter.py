# Author Frank Hu
# Hacker and Painter
# V2.0, 20150331

import simplegui

# initalize globals
# 3 lists for storing different parameters, using index to sync.
WIDTH = 300
HEIGHT = 600
color_in_use = 'Black'
shape_in_use = 'Circle'
shape_list = []
color_list = []
pos_list = []
temp_shape_list = shape_list
temp_color_list = color_list
temp_pos_list = pos_list
interval = 200
time = 0
timer = 0

def paint(canvas):
    # display color and shape in use
    canvas.draw_text('Color in use: %s' % (color_in_use), 
    	             (20, 20), 14, 'Black') 
    canvas.draw_text('Shape in use: %s' % (shape_in_use), 
    	             (20, 40), 14, 'Black') 
    canvas.draw_text('Play interval in use: %s' % (interval),
                     (20, 60), 14, 'Black') 
    i = 0
    while i < len(pos_list):
        if shape_list[i] == 'Circle': # first use "=" instead, a "classic" error
            canvas.draw_circle(pos_list[i], 20, 2, color_list[i])
        elif shape_list[i] == 'Triangle':
            canvas.draw_polygon([(pos_list[i][0],pos_list[i][1] + 20), # ~5*squrt(2)
                                (pos_list[i][0] + 10,pos_list[i][1] - 10),
                                (pos_list[i][0] - 10,pos_list[i][1] - 10)],
                                2, color_list[i])
        else: #i.e.: shape_list == "square" 
            canvas.draw_polygon([(pos_list[i][0] - 15,pos_list[i][1] + 15), # ~5*squrt(2)
                                (pos_list[i][0] + 15,pos_list[i][1] + 15),
                                (pos_list[i][0] + 15,pos_list[i][1] - 15),
                                (pos_list[i][0] - 15,pos_list[i][1] - 15)],
                                2, color_list[i])
        i += 1
    #    print i, len(pos_list), len(color_list)
    # need to use the same index[] when cross-talking in different lists

def click(mouse_click):
    global pos_list
    print mouse_click, color_in_use, shape_in_use
    pos_list.append(mouse_click)
    color_list.append(color_in_use)
    shape_list.append(shape_in_use)
    
def color_setter(color_input):
    global color_in_use
    # need to add robustness here in later version
    color_in_use = color_input
    #label_color.set_text('Color in use: %s') % (color_in_use)

def shape_setter_circle():
    global shape_in_use
    shape_in_use = 'Circle'
    #label_shape.set_text('Shape in use: %s')%(shape_in_use)

def shape_setter_triangle():
    global shape_in_use
    shape_in_use = 'Triangle'
    #label_shape.set_text('Shape in use: %s')%(shape_in_use)

def shape_setter_square():
    global shape_in_use
    shape_in_use = 'Square'
    #label_shape.set_text('Shape in use: %s')%(shape_in_use)

def play():
    # 1: process lists to temp place
    global temp_shape_list
    global temp_color_list 
    global temp_pos_list 
    global shape_list
    global color_list
    global pos_list
    global timer
    temp_shape_list = shape_list
    temp_color_list = color_list
    temp_pos_list = pos_list
    # 2: clear list
    shape_list = []
    color_list = []
    pos_list = []
    # 3: remake list with delay
    print interval
    timer = simplegui.create_timer(interval, tick)
    timer.start()

def tick():
    global time 
    global timer
    if time < len(temp_pos_list):
        shape_list.append(temp_shape_list[time])
        color_list.append(temp_color_list[time])
        pos_list.append(temp_pos_list[time])
        time += 1
        print time        
    else:
        timer.stop()
        time = 0
        print "finished"

def change_interval(interval_input):
    global interval
    interval = int(interval_input)
    print interval

# create frame
frame = simplegui.create_frame('Canvas', WIDTH, HEIGHT)
frame.set_canvas_background('White')
frame.set_draw_handler(paint)

# set event handler
frame.set_mouseclick_handler(click) # get click position
# use a input box to get color
# rewrite it in a label...
frame.add_input('Color: valid input is aqua, black, blue, fuchsia, gray,\
                green, lime, maroon, navy, olive, orange, purple, red,\
                silver, teal, white, yellow. And rgb format #xxx or #xxxxxx,\
                bad input information is shown in canvas', color_setter, 100) 
# 3 buttoms for setting shape
frame.add_button('Circle', shape_setter_circle, 100) 
frame.add_button('Square', shape_setter_square, 100)
frame.add_button('Triangle', shape_setter_triangle, 100)
# button to play whole progress
frame.add_button('Play', play, 100)
frame.add_input('Play interval', change_interval, 100)


#start frame
frame.start()