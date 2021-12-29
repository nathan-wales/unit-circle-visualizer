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

def draw_unit_circle(canvas, x0, y0):
    """Draws the unit circle with a radius of 500.
    
    Arguments:\n
    canvas -- the initialized tkinter canvas to draw the cosine wave on\n
    x0,y0 -- the top left corner x and y coordinates
    """
    radius = 500
    x1 = x0+  radius
    y1 = y0 + radius
    start_angle = 0
    for i in range(4):
        canvas.create_arc(x0, y0, x1, y1, extent=30, start=start_angle, width=2)
        start_angle += 30
        canvas.create_arc(x0, y0, x1, y1, extent=15, start=start_angle, width=2)
        start_angle += 15
        canvas.create_arc(x0, y0, x1, y1, extent=15, start=start_angle, width=2)
        start_angle += 15
        canvas.create_arc(x0, y0, x1, y1, extent=30, start=start_angle, width=2)
        start_angle += 30

    #(0,1)
    canvas.create_text(x1+7, y0 + radius/2, anchor="w",text = "(1,0)")
    canvas.create_text(x0 + radius/2, y0-7, anchor="s",text = "(0,1)")
    canvas.create_text(x0-7, y0 + radius/2, anchor="e",text = "(-1,0)")
    canvas.create_text(x0 + radius/2, y1+7, anchor="n",text = "(0,-1)")

    #sqrt2/2
    canvas.create_text(x1+15, y0+50, anchor="ne", text = "(\u221a2/2, \u221a2/2)")
    canvas.create_text(x1+15, y1-50, anchor="se", text = "(\u221a2/2, -\u221a2/2)")
    canvas.create_text(x0-15, y0+50, anchor="nw", text = "(-\u221a2/2, \u221a2/2)")
    canvas.create_text(x0-15, y1-50, anchor="sw", text = "(-\u221a2/2, -\u221a2/2)")

    #sqrt3, 1/2
    canvas.create_text(x1+45, y0+100, anchor="ne", text = "(\u221a3/2, 1/2)")
    canvas.create_text(x1+45, y1-100, anchor="se", text = "(\u221a3/2, -1/2)")
    canvas.create_text(x0-45, y0+100, anchor="nw", text = "(-\u221a3/2, 1/2)")
    canvas.create_text(x0-45, y1-100, anchor="sw", text = "(-\u221a3/2, -1/2)")

    #1/2, sqrt3
    canvas.create_text(x1-45, y0+10, anchor="ne", text = "(1/2,\u221a3/2)")
    canvas.create_text(x1-45, y1-10, anchor="se", text = "(1/2,-\u221a3/2)")
    canvas.create_text(x0+45, y0+10, anchor="nw", text = "(-1/2,\u221a3/2)")
    canvas.create_text(x0+45, y1-10, anchor="sw", text = "(-1/2,-\u221a3/2)")

def draw_buttons(canvas, x0, y0):
    button_list = ["0", "\u03C0/6", "\u03C0/4", "\u03C0/3"]
    for num in button_list:
        b = tk.Button(canvas, text=num, height=1, width=1)
        b.place(x=x0, y=y0)
        x0 += 50