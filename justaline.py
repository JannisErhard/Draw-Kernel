# Import the required libraries
from tkinter import *

# Create an instance of tkinter frame or window
win=Tk()

# Set the size of the tkinter window
win.geometry("700x350")

# Create a canvas widget
canvas=Canvas(win, width=500, height=300)
canvas.pack()

# Add a line in canvas widget
canvas.create_line(100,200,200,35, fill="green", width=5)
# create_line()
canvas.create_line(1,1,10,10)
canvas.create_line(1+10,1+10,1+100,10+100)
win.mainloop()
