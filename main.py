import tkinter as tk
from draw_helpers import *

def main():
    window = tk.Tk()
    canvas = tk.Canvas(window, bg="white", width=600, height=600)
    draw_cos(canvas, 450, 75, 100, 200)
    draw_sin(canvas, 450, 75, 100, 400)
    canvas.pack()
    window.mainloop()

if __name__ == "__main__":
    main()