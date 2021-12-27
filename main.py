import tkinter as tk
from draw_helpers import *

def main():
    window = tk.Tk()
    canvas = tk.Canvas(window, bg="white", width=1200, height=600)
    draw_cos(canvas, 500, 75, 650, 450)
    draw_sin(canvas, 500, 75, 650, 150)
    draw_unit_circle(canvas, 50, 50, 500)
    canvas.pack()
    window.mainloop()

if __name__ == "__main__":
    main()