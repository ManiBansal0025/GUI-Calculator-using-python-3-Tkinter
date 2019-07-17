# Create Calculator using tkinter
from tkinter import *

window = Tk()
window.title("Calculator")
window.geometry("320x385")
window.configure(bg = "black")

def btnclick(numbers):
     global operators
     operators = operators + str(numbers)
     Text_Input .set (operators)

def btnClearDisp():
     global operators
     operators = " "
     Text_Input.set(" ")

def btnEquals():
     global operators
     operation = str(eval(operators))
     Text_Input.set(operation)
     operators = " " 

operators = " "
Text_Input = StringVar()

etn = Entry(window,font = ("Arial Bold",20), textvariable= Text_Input, bg = "dark green", fg = "white",insertwidth = 7,
            justify = "right",bd=8)
etn.grid(  columnspan = 4)


btn7 = Button(window,font = ("Arial Bold",15),text = "7", bg = "black",fg = "dark green",padx = 15,pady = 15,
              command = lambda:btnclick(7),bd = 8)
btn7.grid(row = 1,column = 0)
btn8 = Button(window,font = ("Arial Bold",15),text = "8", bg = "black",fg = "dark green",padx = 15,pady =15,
              command = lambda:btnclick(8),bd = 8)
btn8.grid(row = 1,column = 1)
btn9 = Button(window,font = ("Arial Bold",15),text = "9", bg = "black",fg = "dark green",padx = 15,pady = 15,
              command = lambda:btnclick(9),bd = 8)
btn9.grid(row = 1,column = 2)
add = Button(window,font = ("Arial Bold",15),text = "+", bg = "black",fg = "dark green",padx = 15,pady = 15,
             command = lambda:btnclick("+"),bd = 8)
add.grid(row = 1,column = 3)


btn4= Button(window,font = ("Arial Bold",15),text = "4", bg = "black",fg = "dark green",padx = 15,pady = 15,
             command = lambda:btnclick(4),bd = 8)
btn4.grid(row = 2,column = 0)
btn5 = Button(window,font = ("Arial Bold",15),text = "5", bg = "black",fg = "dark green",padx = 15,pady = 15,
              command = lambda:btnclick(5),bd = 8)
btn5.grid(row = 2,column = 1)
btn6 = Button(window,font = ("Arial Bold",15),text = "6", bg = "black",fg = "dark green",padx = 15,pady = 15,
              command = lambda:btnclick(6),bd = 8)
btn6.grid(row = 2,column = 2)
sub = Button(window,font = ("Arial Bold",15),text = "-", bg = "black",fg = "dark green",padx = 15,pady = 15,
             command = lambda:btnclick("-"),bd = 8)
sub.grid(row = 2,column = 3)


btn1= Button(window,font = ("Arial Bold",15),text = "1", bg = "black",fg = "dark green",padx = 15,pady = 15,
             command = lambda:btnclick(1),bd = 8)
btn1.grid(row = 3,column = 0)
btn2 = Button(window,font = ("Arial Bold",15),text = "2", bg = "black",fg = "dark green",padx = 15,pady = 15,
              command = lambda:btnclick(2),bd = 8)
btn2.grid(row = 3,column = 1)
btn3 = Button(window,font = ("Arial Bold",15),text = "3", bg = "black",fg = "dark green",padx = 15,pady = 15,
              command = lambda:btnclick(3),bd = 8)
btn3.grid(row = 3,column = 2)
multiply = Button(window,font = ("Arial Bold",15),text = "*", bg = "black",fg = "dark green",padx = 15,pady = 15,
                  command = lambda:btnclick("*"),bd = 8)
multiply.grid(row = 3,column = 3)


btn0 = Button(window,font = ("Arial Bold",15),text = "0", bg = "black",fg = "dark green",padx = 15,pady = 15,
              command = lambda:btnclick(0),bd = 8)
btn0.grid(row = 4,column = 0)
btnClear = Button(window,font = ("Arial Bold",15),text = "C", bg = "black",fg = "dark green",padx = 15,pady = 15,
                  command = btnClearDisp,bd = 8)
btnClear.grid(row = 4,column = 1)
equal = Button(window,font = ("Arial Bold",15),text = "=", bg = "black",fg = "dark green",padx = 15,pady = 15,
               command = btnEquals,bd = 8)
equal.grid(row = 4,column = 2)
divide= Button(window,font = ("Arial Bold",15),text = "/", bg = "black",fg = "dark green",padx = 15,pady = 15,
               command = lambda:btnclick("/"),bd = 8)
divide.grid(row = 4,column = 3)

window.mainloop()
