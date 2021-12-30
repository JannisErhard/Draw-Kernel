#!/usr/bin/env python3
import os
from tkinter import filedialog 

def print_all_segments_to_ASCII_file(all_segments):
    f = open("Segmentfile.txt", 'w')
    for i in range(len(all_segments)):
        f.write(str(all_segments[i])+'\n')
    f.close()
    return 

def read_all_segments_from_ASCII_file_deprecated():
    '''works in body of script, doenst work here as the scope of all_segments ends at EOF'''
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

def read_all_segments_from_ASCII_file():
    ''''''
    tf = filedialog.askopenfilename(
        initialdir=os.getcwd(), 
        title="Open Text file", 
        filetypes=(("Text Files", "*.txt"),)
        )
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
