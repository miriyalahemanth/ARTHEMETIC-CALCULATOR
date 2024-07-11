from tkinter import *
from tkinter import messagebox
window=Tk() 
window.geometry("800x500") 
window.resizable(0,0)
window['bg']='darkgrey'
fn=StringVar()
sn=StringVar()
def addition():
    x=eval(fn.get())
    y=eval(sn.get())
    res=x+y
    messagebox.showinfo("Result",f"the addition of {x} and {y} is: {res}")
def subtraction():
    x=eval(fn.get())
    y=eval(sn.get())
    res=x-y
    messagebox.showinfo("Result",f"the subtraction of {x} and {y} is: {res}")
def multiplication():
    x=eval(fn.get())
    y=eval(sn.get())
    res=x*y
    messagebox.showinfo("Result",f"the multiplication of {x} and {y} is: {res}")
def division():
    x=eval(fn.get())
    y=eval(sn.get())
    res=x/y
    messagebox.showinfo("Result",f"the division of {x} and {y} is: {res}")
def floor_division():
    x=eval(fn.get())
    y=eval(sn.get())
    res=x//y
    messagebox.showinfo("Result",f"the floor_division of {x} and {y} is: {res}")
def modulo():
    x=eval(fn.get())
    y=eval(sn.get())
    res=x%y
    messagebox.showinfo("Result",f"the modulo of {x} and {y} is: {res}")
    
def clear():
    fn.set('')
    sn.set('')
def close():
    window.destroy()
    
L1=Label(window,text="Enter Your First Number:",fg="blue",font="calibri 15 italic")
L1.place(x=50,y=100)
E1=Entry(window,bd=3,font=("forte",15,"bold"),textvariable=fn)
E1.place(x=400,y=100)

L2=Label(window,text="Enter Your Second Number:",fg="blue",font="calibri 15 italic")
L2.place(x=50,y=150)
E2=Entry(window,bd=3,font=("forte",15,"bold"),textvariable=sn)
E2.place(x=400,y=150)

B1=Button(window,text="Add",fg="green",bg="violet",font=("arial",20),
         command=addition)
B1.place(x=50,y=250)

B2=Button(window,text="sub",fg="green",bg="violet",font=("arial",20),
         command=subtraction)
B2.place(x=150,y=250)
B3=Button(window,text="mul",fg="green",bg="violet",font=("arial",20),
         command=multiplication)
B3.place(x=250,y=250)
B4=Button(window,text="div",fg="green",bg="violet",font=("arial",20),
         command=division)
B4.place(x=350,y=250)
B5=Button(window,text="fdiv",fg="green",bg="violet",font=("arial",20),
         command=floor_division)
B5.place(x=450,y=250)
B6=Button(window,text="mod",fg="green",bg="violet",font=("arial",20),
         command=modulo)
B6.place(x=550,y=250)

B7=Button(window,text="clear",fg="green",bg="violet",font=("arial",20),
         command=clear)
B7.place(x=270,y=350)

B8=Button(window,text="Close",fg="green",bg="violet",font=("arial",20),
         command=close)
B8.place(x=450,y=350)

window.mainloop()
