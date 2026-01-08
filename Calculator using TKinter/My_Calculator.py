"""step1:importing """
from tkinter import *

from tkinter import ttk

"""step2: GUI interaction """
window =Tk()
window.geometry('500x500')
window.title("My Calculator")

"""step3:adding inputs """
#Entry box
e=Entry(window,width=56,borderwidth=10)
e.place(x=1,y=2)

#function to get entry input
def num_button(num):
    result=e.get()
    e.delete(0,END)
    e.insert(0,str(result)+str(num))

#buttons
b=Button(window,text='1',width=12,command=lambda:num_button(1),borderwidth=3)
b.place(x=20,y=100)

b=Button(window,text='2',width=12,command=lambda:num_button(2),borderwidth=3)
b.place(x=120,y=100)

b=Button(window,text='3',width=12,command=lambda:num_button(3),borderwidth=3)
b.place(x=220,y=100)

b=Button(window,text='4',width=12,command=lambda:num_button(4),borderwidth=3)
b.place(x=20,y=150)

b=Button(window,text='5',width=12,command=lambda:num_button(5),borderwidth=3)
b.place(x=120,y=150)

b=Button(window,text='6',width=12,command=lambda:num_button(6),borderwidth=3)
b.place(x=220,y=150)

b=Button(window,text='7',width=12,command=lambda:num_button(7),borderwidth=3)
b.place(x=20,y=200)

b=Button(window,text='8',width=12,command=lambda:num_button(8),borderwidth=3)
b.place(x=120,y=200)

b=Button(window,text='9',width=12,command=lambda:num_button(9),borderwidth=3)
b.place(x=220,y=200)

b=Button(window,text='0',width=12,command=lambda:num_button(0),borderwidth=3)
b.place(x=20,y=250)

#Calculator Operators

def add():
    n1=e.get()
    global math
    math="Addition"
    global i
    i=int(n1)
    # n_show=Label(text=f'"{i}" + ')
    # n_show.place(x=20,y=40)
    e.delete(0,END)
b=Button(window,text='+',width=12,command=add,borderwidth=3)
b.place(x=120,y=250)

def Subtract():
    n1=e.get()
    global math
    math="Subtraction"
    global i
    i=int(n1)
    # n_show=Label(text=f'"{i}" - ')
    # n_show.place(x=20,y=40)
    e.delete(0,END)
b=Button(window,text='-',width=12,command=Subtract,borderwidth=3)
b.place(x=220,y=250)

def Multi():
    n1=e.get()
    global math
    math="Multiple"
    global i
    i=int(n1)
    # n_show=Label(text=f'"{i}" * ')
    # n_show.place(x=20,y=40)
    e.delete(0,END)
b=Button(window,text='*',width=12,command=Multi,borderwidth=3)
b.place(x=20,y=300)

def Div():
    n1=e.get()
    global math
    math="Division"
    global i
    i=int(n1)
    # n_show=Label(text=f'"{i}" / ')
    # n_show.place(x=20,y=40)
    e.delete(0,END)
b=Button(window,text='/',width=12,command=Div,borderwidth=3)
b.place(x=120,y=300)

def Equal():
    n2=e.get()
    e.delete(0,END)
    if math=="Addition":
        e.insert(0,i+int(n2))
        # n_show=Label(text=f'"{n2}" = {i+int(n2)}')
        # n_show.place(x=50,y=40)
    elif math=="Subtraction":
        e.insert(0,i-int(n2))
        # n_show=Label(text=f'"{n2}" = {i-int(n2)}')
        # n_show.place(x=50,y=40)
    elif math=="Multiple":
        e.insert(0,i*int(n2))
        # n_show=Label(text=f'"{n2}" = {i*int(n2)}')
        # n_show.place(x=50,y=40)
    elif math=="Division":
        if int(n2)==0:
            e.insert(0,"Can't divide with 0")
        else:
            e.insert(0,i/int(n2))
            # n_show=Label(text=f'"{n2}" = {i/int(n2)}')
            # n_show.place(x=50,y=40)
b=Button(window,text='=',width=12,command=Equal,borderwidth=3)
b.place(x=220,y=300)

def reset():
    e.delete(0,END)
b=Button(window,text='Clear',width=12,command=reset,borderwidth=3)
b.place(x=20,y=350)

""" step4: mainloop"""
mainloop()