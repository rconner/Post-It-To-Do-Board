from tkinter import *


root = Tk()
#Create frame in TK
frame = Frame(root, width=500, height=400)
frame.place()

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
text_1_button = Button(root, width=3, height=1, text = "Clear", command=delete_text1).grid(row=1, column=0, padx=2, pady=2)
my_text2 = Text(root, width=13, height=7, wrap="word")
my_text2.grid(row=0, column=1, padx=10, pady=10)
text_2_button = Button(root, width=3, height=1, text = "Clear", command=delete_text2).grid(row=1, column=1, padx=2, pady=2)
my_text3 = Text(root, width=13, height=7, wrap="word")
my_text3.grid(row=0, column=2, padx=10, pady=10)
text_3_button = Button(root, width=3, height=1, text = "Clear", command=delete_text3).grid(row=1, column=2, padx=2, pady=2)
my_text4 = Text(root, width=13, height=7, wrap="word")
my_text4.grid(row=2, column=0, padx=10, pady=10)
text_4_button = Button(root, width=3, height=1, text = "Clear", command=delete_text4).grid(row=3, column=0, padx=2, pady=2)
my_text5 = Text(root, width=13, height=7, wrap="word")
my_text5.grid(row=2, column=1, padx=10, pady=10)
text_5_button = Button(root, width=3, height=1, text = "Clear", command=delete_text5).grid(row=3, column=1, padx=2, pady=2)
my_text6 = Text(root, width=13, height=7, wrap="word")
my_text6.grid(row=2, column=2, padx=10, pady=10)
text_6_button = Button(root, width=3, height=1, text = "Clear", command=delete_text6).grid(row=3, column=2, padx=2, pady=2)
my_text7 = Text(root, width=13, height=7, wrap="word")
my_text7.grid(row=4, column=0, padx=10, pady=10)
text_7_button = Button(root, width=3, height=1, text = "Clear", command=delete_text7).grid(row=5, column=0, padx=2, pady=2)
my_text8 = Text(root, width=13, height=7, wrap="word")
my_text8.grid(row=4, column=1, padx=10, pady=10)
text_8_button = Button(root, width=3, height=1, text = "Clear", command=delete_text8).grid(row=5, column=1, padx=2, pady=2)
my_text9 = Text(root, width=13, height=7, wrap="word")
my_text9.grid(row=4, column=2, padx=10, pady=10)
text_9_button = Button(root, width=3, height=1, text = "Clear", command=delete_text9).grid(row=5, column=2, padx=2, pady=2)
my_text10 = Text(root, width=13, height=7, wrap="word")
my_text10.grid(row=6, column=0, padx=10, pady=10)
text_10_button = Button(root, width=3, height=1, text = "Clear", command=delete_text10).grid(row=7, column=0, padx=2, pady=2)
my_text11 = Text(root, width=13, height=7, wrap="word")
my_text11.grid(row=6, column=1, padx=10, pady=10)
text_11_button = Button(root, width=3, height=1, text = "Clear", command=delete_text11).grid(row=7, column=1, padx=2, pady=2)
my_text12 = Text(root, width=13, height=7, wrap="word")
my_text12.grid(row=6, column=2, padx=10, pady=10)
text_12_button = Button(root, width=3, height=1, text = "Clear", command=delete_text12).grid(row=7, column=2, padx=2, pady=2)






#def callback():
    #x = my_text3.get()
    #print(x)
    

#bottom = Frame(root)    # Create frame to hold button
#bottom.grid()           # Pack bottom frame
#b = Button(bottom, text="Clear", command=clear)
#b.grid()

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

