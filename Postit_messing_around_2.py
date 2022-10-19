

from tkinter import *
root = Tk()

top = Frame(root)   # Create frame to hold entrys
top.pack()          # Pack top frame
l1 = Label(top, text="Variable_1")
l1.pack(side=LEFT)
e1 = Entry(top, bd=5)
e1.pack(side=LEFT)

l2 = Label(top, text="Variable_2")
l2.pack(side=LEFT)
e2 = Entry(top, bd=5)
e2.pack(side=LEFT)

l = Label(root)
def callback():
    x = e1.get()
    y = e2.get()
    print(x)
    print(y)

bottom = Frame(root)    # Create frame to hold button
bottom.pack()           # Pack bottom frame
b = Button(bottom, text="OK", command=callback)
b.pack()

mainloop()

