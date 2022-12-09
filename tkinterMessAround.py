import tkinter as tk
from tkinter import ttk
from random import randrange
from tkinter import *


root = Tk()
#my_w = Tk()
width, height = 355,710 #set variables
d=str(width) + "x" + str(height+40)
root = tk.Canvas(root, width=width-10, height = height-10)
root.grid(row=0, column=0,padx=5,pady=5)
x1, y1, x2, y2 = 5, 5, width-5, height-5
gap = 25
#Create frame in TK
frame = Frame(root, width=500, height=400)
frame.place()
#root.title("Post It To Do's")

def my_draw():
   global x1, y1, x2, y2
   color_c='#%02x%02x%02x' % (randrange(256), randrange(256), randrange(256))
   root.create_rectangle(x1, y1, x2, y2, fill = color_c)
   x1, y1, x2, y2 = x1+gap, y1+gap, x2-gap, y2-gap
   print(x1)

   if (x1<(width/2)):
      root.after(500, my_draw)
   else:
      return
my_draw()


font_tuple = ("Great Vibes", 9, "normal")

# create buttons under row within grid - adjust padding for smaller buttons. row 0 col 0 widget row 1 column 0 button
#make clear method for each button
#look at pillow for images
#Create Clear Function
def delete_text1():
   my_text1.delete("1.0", "end")
def delete_text2():
    my_text2.delete("1.0", "end")
def delete_text3():
   my_text3.delete("1.0", "end")
def delete_text4():
   my_text4.delete("1.0", "end")
def delete_text5():
   my_text5.delete("1.0", "end")
def delete_text6():
   my_text6.delete("1.0", "end")
def delete_text7():
   my_text7.delete("1.0", "end")
def delete_text8():
   my_text8.delete("1.0", "end")
def delete_text9():
   my_text9.delete("1.0", "end")
def delete_text10():
   my_text10.delete("1.0", "end")
def delete_text11():
   my_text11.delete("1.0", "end")
def delete_text12():
   my_text12.delete("1.0", "end")

#Create text box dimensions
my_text1 = Text(root, width=13, height=7, wrap="word")
my_text1.grid(row=0, column=0, padx=10, pady=10)
my_text1.configure(font = font_tuple, fg = 'black', bg = 'white')
#my_text1.lift()
text_1_button = Button(root, width=4, height=1, text = "Clear", command=delete_text1)
text_1_button.grid(row=1, column=0, padx=2, pady=2)
#text_1_button.lift()
my_text2 = Text(root, width=13, height=7, wrap="word")
my_text2.grid(row=0, column=1, padx=10, pady=10)
my_text2.configure(font = font_tuple, fg = 'black', bg = 'white')
#my_text2.lift()
text_2_button = Button(root, width=4, height=1, text = "Clear", command=delete_text2)
text_2_button.grid(row=1, column=1, padx=2, pady=2)
#my_text2.lift()
my_text3 = Text(root, width=13, height=7, wrap="word")
my_text3.grid(row=0, column=2, padx=10, pady=10)
my_text3.configure(font = font_tuple, fg = 'black', bg = 'white')
text_3_button = Button(root, width=4, height=1, text = "Clear", command=delete_text3).grid(row=1, column=2, padx=2, pady=2)
my_text4 = Text(root, width=13, height=7, wrap="word")
my_text4.grid(row=2, column=0, padx=10, pady=10)
my_text4.configure(font = font_tuple, fg = 'magenta', bg = 'white')
text_4_button = Button(root, width=4, height=1, text = "Clear", command=delete_text4).grid(row=3, column=0, padx=2, pady=2)
my_text5 = Text(root, width=13, height=7, wrap="word")
my_text5.grid(row=2, column=1, padx=10, pady=10)
my_text5.configure(font = font_tuple, fg = 'cyan', bg = 'white')
text_5_button = Button(root, width=4, height=1, text = "Clear", command=delete_text5).grid(row=3, column=1, padx=2, pady=2)
my_text6 = Text(root, width=13, height=7, wrap="word")
my_text6.grid(row=2, column=2, padx=10, pady=10)
my_text6.configure(font = font_tuple, fg = 'yellow', bg = 'white')
text_6_button = Button(root, width=4, height=1, text = "Clear", command=delete_text6).grid(row=3, column=2, padx=2, pady=2)
my_text7 = Text(root, width=13, height=7, wrap="word")
my_text7.grid(row=4, column=0, padx=10, pady=10)
my_text7.configure(font = font_tuple, fg = 'yellow', bg = 'white')
text_7_button = Button(root, width=4, height=1, text = "Clear", command=delete_text7).grid(row=5, column=0, padx=2, pady=2)
my_text8 = Text(root, width=13, height=7, wrap="word")
my_text8.grid(row=4, column=1, padx=10, pady=10)
my_text8.configure(font = font_tuple, fg = 'magenta', bg = 'white')
text_8_button = Button(root, width=4, height=1, text = "Clear", command=delete_text8).grid(row=5, column=1, padx=2, pady=2)
my_text9 = Text(root, width=13, height=7, wrap="word")
my_text9.grid(row=4, column=2, padx=10, pady=10)
my_text9.configure(font = font_tuple, fg = 'cyan', bg = 'white')
text_9_button = Button(root, width=4, height=1, text = "Clear", command=delete_text9).grid(row=5, column=2, padx=2, pady=2)
my_text10 = Text(root, width=13, height=7, wrap="word")
my_text10.grid(row=6, column=0, padx=10, pady=10)
my_text10.configure(font = font_tuple, fg = 'cyan', bg = 'white')
text_10_button = Button(root, width=4, height=1, text = "Clear", command=delete_text10).grid(row=7, column=0, padx=2, pady=2)
my_text11 = Text(root, width=13, height=7, wrap="word")
my_text11.grid(row=6, column=1, padx=10, pady=10)
my_text11.configure(font = font_tuple, fg = 'yellow', bg = 'white')
text_11_button = Button(root, width=4, height=1, text = "Clear", command=delete_text11).grid(row=7, column=1, padx=2, pady=2)
my_text12 = Text(root, width=13, height=7, wrap="word")
my_text12.grid(row=6, column=2, padx=10, pady=10)
my_text12.configure(font = font_tuple, fg = 'magenta', bg = 'white')
text_12_button = Button(root, width=4, height=1, text = "Clear", command=delete_text12).grid(row=7, column=2, padx=2, pady=2)


mainloop()

