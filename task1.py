#! python3
""" 
Create a binary converter.
Recall that binary is a system of counting based on powers of 2.
00000001 = 1
00000010 = 2
00001110 = 14

Create a converter that will convert binary to decimal or decimal to
binary using the interface shown in task1.png.  Use the shell that
has been started in task1.py
This is an incomplete program.  You will need to add onto it, 
but you should not change any of the commands that are already 
here

Use assignment_test.py to test your functions
"""


import tkinter as tk 
from tkinter import *

win = tk.Tk()
win.geometry("200x100")

r1 = IntVar()
r1.set(0)
r2 = IntVar()
r2.set(0)
r3 = IntVar()
r3.set(0)
r4 = IntVar()
r4.set(0)
r5 = IntVar()
r5.set(0)
r6 = IntVar()
r6.set(0)
r7 = IntVar()
r7.set(0)
r8 = IntVar()
r8.set(0)

def binary_to_decimal(binary):
    # binary is a tuple of length 8
    # return value is an integer decimal
    binary = ''.join(str(i) for i in binary)
    decimal = int(binary,2)
    return decimal 

def decimal_to_binary(decimal):
    # decimal is an integer value
    # binary is a tuple of length 8 that contains 1's and 0's
    binary = bin(decimal)
    binary = list(binary)
    binary = ','.join(str(i) for i in binary)
    binary = binary.split(",")
    if len(binary) < 10:
        for m in range(10 - len(binary)):
            binary.insert(2,0)
    return binary


def get_binary():
    # function should read the entry widget and generate an integer
    # this integer will be used as an input parameter for decimal to binary and the result updated
    # in the 8 checkboxes
    decimal = int(op.get())
    binary = binary_to_decimal(decimal)
    r1.set(binary[9])
    r2.set(binayr[8])
    r3.set(binary[7])
    r4.set(binary[6])
    r5.set(binary[5])
    r6.set(binary[4])
    r7.set(binary[3])
    r8.set(binary[2])


def get_decimal():
    # function should read the checkboxes and generate a tuple called binary of length 8 that has 1's and 0's
    # this tuple will be used as an input parameter for binary_to_decimal and the result updated
    # in the entry box
    binary = [r8.get(),r7.get(),r6.get(),r5.get(),r4.get(),r3.get(),r2.get(),r1.get()]
    decimal = binary_to_decimal(binary)
    e1.delete(0,END)
    e1.insert(0,decimal)

op = StringVar()
op.set("")

l1 = Label(win,text = "Binary / Decimal Converter!")
b1 = Button(win, text="Convert to Binary", command=get_binary)
b2 = Button(win, text="Convert to Decimal", command=get_decimal)
e1 = Entry(win,width = 20,textvariable = op)
cb1 = Checkbutton(win,variable = r1)
cb2 = Checkbutton(win,variable = r2)
cb3 = Checkbutton(win,variable = r3)
cb4 = Checkbutton(win,variable = r4)
cb5 = Checkbutton(win,variable = r5)
cb6 = Checkbutton(win,variable = r6)
cb7 = Checkbutton(win,variable = r7)
cb8 = Checkbutton(win,variable = r8)

cb8.grid(row = 2,column = 1)
cb7.grid(row = 2,column = 2)
cb6.grid(row = 2,column = 3)
cb5.grid(row = 2,column = 4)
cb4.grid(row = 2,column = 5)
cb3.grid(row = 2,column = 6)
cb2.grid(row = 2,column = 7)
cb1.grid(row = 2,column = 8)
l1.grid(row = 1,column = 1,columnspan = 8)
b1.grid(row = 3,column = 1,columnspan = 4)
b2.grid(row = 3,column = 5,columnspan = 4)
e1.grid(row = 4,column = 1,columnspan = 8)

win.mainloop()
