#!/usr/bin/env python3
from tkinter import *

root = Tk()

def callback(*args):
    print("Motion detected")

frame = Frame(root, width=100, height=100)

frame.bind("<Motion>", callback)

frame.pack()

root.mainloop()
