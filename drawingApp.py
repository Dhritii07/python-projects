'''
features:
- brush selection
- brush size selection
- eraser selection
- eraser size selection
- multiple color selections for background and drawing as well
- clear the drawing 
- saving the image
'''

import time
from tkinter import *
import tkinter as tk
from tkinter import filedialog
import PIL.ImageGrab as ImageGrab  #used for grabbing ss of selected portion
from tkinter import colorchooser, messagebox

#main: new tkinter window
window = Tk()
window.title('Drawing App')

def select_brush():
    global selected_color
    selected_color = previous_color 

def change_brush_size():
    global brush_size 
    brush_size = int(value)

def select_brush_size():
    pass

def select_eraser():
    pass

def select_eraser_size():
    pass

def select_brush_color():
    pass

def select_background_color():
    pass

def clear_canavs():
    pass

def save_image():
    pass

#menu bar
menu_bar = Menu(window)

#brush menu
brush_menu = Menu(menu_bar, tearoff=0)
brush_menu.add_command(label='Select Brush', command=select_brush)
brush_menu.add_command(label='Select Brush Size', command=select_brush_size)

#eraser menu
eraser_menu = Menu(menu_bar, tearoff=0)
eraser_menu.add_command(label='Select Eraser', command=select_eraser)
brush_menu.add_command(label='Select Eraser Size', command=select_eraser_size)

#color menu
color_menu = Menu(menu_bar, tearoff=0)
color_menu.add_command(label='Select Drawing Color', command=select_brush_color)
color_menu.add_command(label='Select Background Color', command=select_background_color)

#clear menu
clear_menu = Menu(menu_bar, tearoff=0)
clear_menu.add_command(label='Clear Canvas', command=clear_canavs)

#save 
save_menu = Menu(menu_bar, tearoff=0)
save_menu.add_command(label='Save Drawing', command=save_image)

#menu bar
menu_bar.add_cascade(label='Brush', menu=brush_menu)
menu_bar.add_cascade(label='Eraser', menu=eraser_menu)
menu_bar.add_cascade(label='Color', menu=color_menu)
menu_bar.add_cascade(label="Clear", menu=clear_menu)
menu_bar.add_cascade(label="Save", menu=save_menu)

window.config(menu=menu_bar)
canvas = Canvas(window, width=800, height=480, bg='white')
canvas.pack()
window.mainloop()