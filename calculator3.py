from tkinter import *
import math


root = Tk()
root.resizable(True, True)
root.title("Calculator Prototype")

def click(number):
    current = ent.get()
    ent.delete(0, END)
    return(ent.insert(0, str(current) + str(number)))

def clear():
    ent.delete(0, END)


def add():
    first_num = ent.get()
    global fff
    fff = int(first_num)
    global operation
    operation = "addition"
    ent.delete(0, END)
    
def subtract():
    first_num = ent.get()

    global fff
    fff = int(first_num)
    global operation
    operation = "subtraction"
    ent.delete(0, END)
    
def multiply():
    first_num = ent.get()
    global fff
    fff = int(first_num)
    global operation
    operation = "multiplication"
    ent.delete(0, END)


def divide():
    first_num = ent.get()
    global fff
    fff = int(first_num)
    global operation
    operation = "division"
    ent.delete(0, END)
    
def sine():
    first_num = ent.get()
    global fff
    fff = int(first_num)
    global operation
    operation = "sine"
    ent.delete(0, END)


def equal():
    global second_num
    second_num = ent.get()
    sss = int(second_num)
    ent.delete(0, END)
    global boom
    if operation == "addition":
        boom = fff + sss
    if operation == "subtraction":
        boom = fff - sss
    if operation == "multiplication":
        boom = fff * sss
    if operation == "division":
        boom = fff / sss
    if operation == "sine":
        boom = math.sin(fff)
    ent.insert(0, boom)

ent = Entry(width=60)
btn1 = Button(text=1,width=15,padx=7,pady=5, command=lambda: click(1))
btn2 = Button(text=2,width=15,padx=7,pady=5, command=lambda:click(2))
btn3 = Button(text=3,width=15,padx=7,pady=5, command=lambda:click(3))
btn4 = Button(text=4,width=15,padx=7,pady=5, command=lambda:click(4))
btn5 = Button(text=5,width=15,padx=7,pady=5, command=lambda:click(5))
btn6 = Button(text=6,width=15,padx=7,pady=5, command=lambda:click(9))
btn7 = Button(text=7,width=15,padx=7,pady=5, command=lambda:click(7))
btn8 = Button(text=8,width=15,padx=7,pady=5, command=lambda:click(8))
btn9 = Button(text=9,width=15,padx=7,pady=5, command=lambda:click(9))
btn0 = Button(text=0,width=15,padx=7,pady=5, command=lambda:click(0))


btn_clear = Button(text="Clear",width=25,padx=13,pady=5, command=lambda:clear())
btn_add = Button(text="+",width=25,padx=13,pady=5, command=lambda:add())
btn_subtract = Button(text="-",width=25,padx=13,pady=5, command=lambda:subtract())
btn_multiply = Button(text="*",width=25,padx=13,pady=5, command=lambda:multiply())
btn_divide = Button(text="/",width=25,padx=13,pady=5, command=lambda:divide())
btn_sine = Button(text="sine",width=25,padx=13,pady=5, command=lambda:sine())
btn_equal = Button(text="=",width=25,padx=13,pady=5, command=lambda:equal())




ent.grid(row=0, column=0, columnspan=3)
btn1.grid(row=1,column=0)
btn2.grid(row=1,column=1)
btn3.grid(row=1,column=2)

btn4.grid(row=2,column=0)
btn5.grid(row=2,column=1)
btn6.grid(row=2,column=2)

btn7.grid(row=3,column=0)
btn8.grid(row=3,column=1)
btn9.grid(row=3,column=2)
btn0.grid(row=4,column=3)

btn_clear.grid(row=4, column=0, columnspan=2)
btn_add.grid(row=5, column=0, columnspan=2)
btn_subtract.grid(row=6, column=0, columnspan=2)
btn_multiply.grid(row=7, column=0, columnspan=2)
btn_sine.grid(row=7, column=0, columnspan=2)
btn_divide.grid(row=8, column=0, columnspan=2)


btn_equal.grid(row=9, column=0, columnspan=2)
root.mainloop()