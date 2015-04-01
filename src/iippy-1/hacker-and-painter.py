# Author Frank Hu
# Hacker and Painter
# V1.0, 20150331

import simplegui

# initalize globals
# 3 lists for storing different parameters, using index to sync.
WIDTH = 300
HEIGHT = 200
color_in_use = 'Black'
# a element in these lists to defend index out of range?
i = 0
shape_list = []
color_list = []
pos_list = []

def paint(canvas):
    #for mouse_click in pos_list:
    #    canvas.draw_circle(mouse_click, 20, 1, "Black")
    # i = 1, trick here: a safe init to defend index out of range?
    global i
    while i < int(len(pos_list)):
        canvas.draw_circle(pos_list[i], 20, 1, color_list[i])
        i += 1
        print int(i), int(len(pos_list))
        print pos_list


    # need to use the same index[] when cross-talking in different lists
    # any data structure like structure in C in python?

def click(mouse_click):
    global pos_list
    global i
    print mouse_click
    i = 0
    pos_list.append(mouse_click)
    color_list.append(color_in_use)
    
# create frame
frame = simplegui.create_frame("Canvas", WIDTH, HEIGHT)
frame.set_canvas_background("White")

# set event handler
frame.set_mouseclick_handler(click)
frame.set_draw_handler(paint)

#start frame
frame.start()