import tkinter as tk
import math

def draw_chart(canvas, width, scale, xstart, ystart):
    #draw the axis
    height_above_axis = ystart + math.cos(0) * scale * 1.3
    height_below_axis = ystart - math.cos(0) * scale * 1.3
    posOne = ystart + math.cos(0) * scale
    negOne = ystart - math.cos(0) * scale
    canvas.create_line(xstart, ystart, xstart + width, ystart, width = 2) #x axis
    canvas.create_line(xstart, height_above_axis , xstart, height_below_axis, width=2) #y axis
    canvas.create_line(xstart -5, posOne, xstart + 5, posOne, width = 3) # pos one label
    canvas.create_line(xstart -5, negOne, xstart + 5, negOne, width = 3) # neg one label
    canvas.create_text(xstart - 12, posOne, anchor=tk.CENTER, text="1")
    canvas.create_text(xstart - 12, negOne, anchor=tk.CENTER, text="-1")

def draw_sin(canvas, width, scale, xstart, ystart, include_chart=True):
    """Draw a sine wave on the given tkinter canvas from 0 to 2pi.
    
    Arguments:\n
    canvas -- the initialized tkinter canvas to draw the sine wave on\n
    width -- the width of the full sine wave in px desired\n
    scale -- the vertical scale of the wave\n
    xstart -- the starting x position in pixels\n
    ystart -- the y position of the axis\n
    """

    scale = -1 * scale #make scale negative for drawing math

    if include_chart: draw_chart(canvas, width, scale, xstart, ystart)

    tau = 2 * math.pi
    prev_y = ystart
    for i in range(1,width):
        increment = tau / width * i
        y2 = ystart + math.sin(increment) * scale
        canvas.create_line(xstart, prev_y, xstart+1, y2, width=2)
        xstart += 1
        prev_y = y2

def draw_cos(canvas, width, scale, xstart, ystart, include_chart=True):
    """Draw a cosine wave on the given tkinter canvas from 0 to 2pi.
    
    Arguments:\n
    canvas -- the initialized tkinter canvas to draw the cosine wave on\n
    width -- the width of the full sine wave in px desired\n
    scale -- the vertical scale of the wave\n
    xstart -- the starting x position in pixels\n
    ystart -- the y position of the axis\n
    """
    scale = -1 * scale #make scale negative for drawing math

    if include_chart: draw_chart(canvas, width, scale, xstart, ystart)
    
    tau = 2 * math.pi
    prev_y = ystart + math.cos(0) * scale
    for i in range(1,width):
        increment = tau / width * i
        y2 = ystart + math.cos(increment) * scale
        canvas.create_line(xstart, prev_y, xstart+1, y2, width=2)
        xstart += 1
        prev_y = y2