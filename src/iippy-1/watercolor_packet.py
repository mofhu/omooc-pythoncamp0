# -*- coding: utf-8 -*-
# Author Frank Hu
# Hacker and Painter, watercolor version
# V3.0-packet, 20150422

import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

# initalize globals
color_in_use = 'rgb(0,255,255)'
pixel_list = []

class Drawing:
    # class for a single draw action
    # note: type of painter maybe added in later version.
    def __init__(self, color, position, size):
        self.color = color
        self.position = position
        self.size = size

    def __str__(self): # print for debugging
        return self.color, self.position, self.size

    def draw_pixel(self):
    # draw by append every pixel in the single drawing to pixel list
        i = 0 - self.size
        while i < self.size:
            j = 0 - self.size
            while j < self.size:
                distence = i * i + j * j
                if distence < self.size * self.size:
                    drawing_color_CMYK = RGB_to_CMYK(self.color)
                    new_pixel = Pixel(CMYK_to_RGB(watercolor(drawing_color_CMYK, self.size * self.size, distence)), 
                                      [self.position[0] + i, self.position[1] + j])
                    new_pixel.draw(pixel_list)
                j += 1
            i += 1

class Pixel:
    # class for a single pixel, storing its color and position
    # may be defined as a single pixel Drawing.
    def __init__(self, color, position):
        self.color = color
        self.position = position
        
    def __str__(self): # print for debugging
        return str(self.color), str(self.position)
        
    def draw(self, pixel_list):        
        for i in pixel_list:
            if i.position == self.position: 
            # i.e. there are something in the new pixel, need to merge color
                # first converse RGB to CMYK;
                # then merge CMYK;
                # final transfer back to RGB;
                # i.color = (r, g, b). i.e. a tuple with 3 elements 
                i.color = CMYK_to_RGB(merge_CMYK(RGB_to_CMYK(i.color), 
                                      RGB_to_CMYK(self.color)))
                return pixel_list        
        pixel_list.append(self)
        return pixel_list

def paint(canvas): 
    # main print function
    for i in pixel_list:
        canvas.draw_point(i.position, i.color)
    canvas.draw_text('Color in use: %s' % (color_in_use), 
                     (20, 20), 14, 'Black') 
    canvas.draw_polygon([(210, 5), (230,5), (230,25), (210,25)], 
                        1, color_in_use, color_in_use)

def watercolor(color_CMYK, shape_size, distence):
    # calculate the distence / max size ratio
    watercolor_ratio = float(shape_size - distence) / shape_size
    return (float(color_CMYK[0]) * watercolor_ratio, 
            float(color_CMYK[1]) * watercolor_ratio,
            float(color_CMYK[2]) * watercolor_ratio, 
            float(color_CMYK[3]) * watercolor_ratio)

def RGB_to_CMYK(color_RGB):
    # the format is 'rgb(r,g,b)', cut rgb(), then translate into a int tuple
    color_RGB_cut = color_RGB.strip('rgb()')
    color_RGB_tuple = color_RGB_cut.split(',')
    color_R = float(int(color_RGB_tuple[0])) / 255
    color_G = float(int(color_RGB_tuple[1])) / 255
    color_B = float(int(color_RGB_tuple[2])) / 255
    color_K = 1 - max(color_R, color_G, color_B)
    if color_K == 1:
        # a special case: 1 - K = 0
        return (0, 0, 0, 1)
    else:
        return ((1 - color_R - color_K) / (1 - color_K), 
                (1 - color_G - color_K) / (1 - color_K), 
                (1 - color_B - color_K) / (1 - color_K),
                color_K)

def merge_CMYK(color_1, color_2):
    return (max(color_1[0], color_2[0]), max(color_1[1], color_2[1]),
            max(color_1[2], color_2[2]), max(color_1[3], color_2[3]))

def CMYK_to_RGB(color_CMYK):
    # R = 255(1-C)(1-K); G = 255(1-M)(1-K); B = 255(1-Y)(1-K)
    color_R = int((255 * (1 - color_CMYK[0]) * (1 - color_CMYK[3])))
    color_G = int((255 * (1 - color_CMYK[1]) * (1 - color_CMYK[3])))
    color_B = int((255 * (1 - color_CMYK[2]) * (1 - color_CMYK[3])))
    return 'rgb' + str((color_R, color_G, color_B))
    # return format 'rgb(r,g,b)'

