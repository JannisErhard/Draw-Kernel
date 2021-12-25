#!/usr/bin/env python3
from tkinter import *
#from tkinter.colorchooser import askcolor


class Kernel(object):

    def draw(self, event):
        print(self.x_0, self.y_0, type(self.c))
        if self.x_0 and self.y_0:
            self.c.create_line(self.x_0, self.y_0, event.x, event.y)
        self.x_0 = event.x
        self.y_0 = event.y

    def letgo(self, event):
        self.x_0, self.y_0 = None, None

    def __init__(self):
        self.root = Tk()
        self.c = Canvas(self.root, bg='white', width=200, height=400)
        self.c.grid(row=1, columnspan=5)
        self.x_0 = None
        self.y_0 = None
        self.c.bind('<B1-Motion>', self.draw)
        self.c.bind('<ButtonRelease-1>', self.letgo)
        self.root.mainloop()



if __name__ == '__main__':
    Kernel()
