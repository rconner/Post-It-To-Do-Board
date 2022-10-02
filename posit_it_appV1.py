from tkinter import *
from turtle import clear

from setuptools import Command

root = Tk()
#Create frame in TK
frame = Frame(root, width=500, height=400)
frame.pack()

#Create text box dimensions
my_text1 = Text(root, width=13, height=7, wrap="word")
my_text1.pack(pady=20)

#Create Clear Function
def clear():
   my_text.delete(1.0, END)

#Tell button where to be
bottomframe = Frame(root)
bottomframe.pack( side = BOTTOM)

#Created a 2nd text box
my_text2 = Text(root, width=13, height=7, wrap="word")
my_text2.pack(pady=40)

#Told it to go to the top but it just went to the top of the other textbox
topframe = Frame(root)
topframe.pack( side = TOP)


#Create blear screen button
clear_button = Button(bottomframe, text="clear Screen", command= clear)
clear_button.grid(row=0, column=0)


mainloop()

