from tkinter import *
from turtle import clear

from setuptools import Command

root = Tk()
#Create frame in TK
frame = Frame(root, width=500, height=400)
frame.place()

#Create text box dimensions
my_text1 = Text(root, width=13, height=7, wrap="word").grid(row=0, column=0, padx=10, pady=10)
my_text2 = Text(root, width=13, height=7, wrap="word").grid(row=0, column=1, padx=10, pady=10)
my_text3 = Text(root, width=13, height=7, wrap="word").grid(row=0, column=2, padx=10, pady=10)
my_text4 = Text(root, width=13, height=7, wrap="word").grid(row=1, column=0, padx=10, pady=10)

my_text5 = Text(root, width=13, height=7, wrap="word").grid(row=1, column=1, padx=10, pady=10)
my_text6 = Text(root, width=13, height=7, wrap="word").grid(row=1, column=2, padx=10, pady=10)
my_text7 = Text(root, width=13, height=7, wrap="word").grid(row=2, column=0, padx=10, pady=10)
my_text8 = Text(root, width=13, height=7, wrap="word").grid(row=2, column=1, padx=10, pady=10)

my_text9 = Text(root, width=13, height=7, wrap="word").grid(row=2, column=2, padx=10, pady=10)
my_text10 = Text(root, width=13, height=7, wrap="word").grid(row=3, column=0, padx=10, pady=10)
my_text11 = Text(root, width=13, height=7, wrap="word").grid(row=3, column=1, padx=10, pady=10)
my_text12 = Text(root, width=13, height=7, wrap="word").grid(row=3, column=2, padx=10, pady=10)
#Create Clear Function
def clear():
   my_text1.delete(1.0, END)


def callback():
    x = my_text3.get()
    y = my_text3.get()
    print(x)
    print(y)

bottom = Frame(root)    # Create frame to hold button
bottom.grid()           # Pack bottom frame
b = Button(bottom, text="Clear", command=callback)
b.grid()

#Tell button where to be
#bottomframe = Frame(root)
#bottomframe.pack( side = BOTTOM)

#Created a 2nd text box
#my_text2 = Text(root, width=13, height=7, wrap="word").grid(row=0, column=1)
#my_text2.pack(width=10).grid(row=0, column=1)

#Told it to go to the top but it just went to the top of the other textbox
#topframe = Frame(root)
#topframe.pack( side = TOP)


#Create clear screen button
#clear_button = Button(bottomframe, text="clear Screen", command= clear)
#clear_button.grid(row=0, column=0)


mainloop()

