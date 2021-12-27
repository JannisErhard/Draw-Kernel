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
    global x_0, y_0, all_segments 
    all_segment_ids = w.find_all()
    all_segments = []
    for isegment in range(len(all_segment_ids)):
        all_segments.append(w.coords(isegment))
#    print(all_segments)
    x_0, y_0 = None, None

def print_all_segments_to_shell():
    global all_segments 
    for i in range(len(all_segments)):
         print(all_segments[i])
    return 

def print_all_segments_to_ASCII_file():
    global all_segments 
    f = open("Segmentfile.txt", 'w')
    for i in range(len(all_segments)):
        f.write(str(all_segments[i])+'\n')
    f.close()
    return 

def read_all_segments_from_ASCII_file():
    global all_segments 
    all_segments = []
    four_integers = []
    with open("Segmentfile.txt", "r") as f:
        aux  = f.read()
    for i in range(len((aux.split('\n')))):
        fourtuple = (aux.split('\n'))[i]
        four_integers_as_characters = fourtuple.replace(',','').replace('[','').replace(']','')
        if len(four_integers_as_characters.split()) == 4:
            a,b,c,d = map(float,(four_integers_as_characters.split()))
            tuple_of_four_integers_as_floats = a,b,c,d
            four_integers_as_floats = list(tuple_of_four_integers_as_floats)
            all_segments.append(four_integers_as_floats)
    f.close()
    return 

def draw_set_to_canvas():
    global all_segments 
    for i in range(len(all_segments)):
        w.create_line(all_segments[i])

master = Tk()

x_0 = None
y_0 = None

# setup drawing
w = Canvas(master, width=500, height=500)
w.bind('<B1-Motion>', draw)
w.bind('<ButtonRelease-1>', letgo)
w.grid(row=1,columnspan=5)

# setup buttons
button_print_to_shell = Button(master, text="Print To Shell", command = print_all_segments_to_shell )
button_print_to_shell.grid(row=0, column=0)
button_print_to_file = Button(master, text="Print To File", command = print_all_segments_to_ASCII_file )
button_print_to_file.grid(row=0, column=1)
button_read_from_ASCII_file = Button(master, text="Read from File", command = read_all_segments_from_ASCII_file )
button_read_from_ASCII_file.grid(row=0, column=2)
button_draw_set_to_canvas = Button(master, text="Draw Set to Canvas", command = draw_set_to_canvas )
button_draw_set_to_canvas.grid(row=0, column=3)



all_ids = w.find_all()
print(all_ids)
mainloop()