#!/usr/bin/env python3
from tkinter import *
    
global x_0, y_0
    
def draw(event):
    global x_0, y_0
    if x_0 and y_0:
        w.create_line(x_0, y_0, event.x, event.y)
    x_0 = event.x
    y_0 = event.y

def letgo(event):
    global x_0, y_0
    all_segment_ids = w.find_all()
    all_segments = []
    for isegment in range(len(all_segment_ids)):
        all_segments.append(w.coords(isegment))
    print(all_segments)
    x_0, y_0 = None, None

master = Tk()
w = Canvas(master, width=500, height=500)
w.pack()
x_0 = None
y_0 = None
w.bind('<B1-Motion>', draw)
w.bind('<ButtonRelease-1>', letgo)

mainloop()