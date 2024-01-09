from tkinter import *
from random import randint
window=Tk()
window.title("Password Generator By Mahearsh")
window.iconbitmap(r'pswd.ico')
window.geometry("500x300")


def new_rand():
    e2.delete(0,END)
    pl=int(e1.get())
    p=''
    for a in range(pl):
        p+=chr(randint(33,126))

    e2.insert(0,p)

    
lf=LabelFrame(window,text="How Many Characters ?")
e1=Entry(lf,font=("Ariel",24))
e1.pack(padx=20,pady=20)
lf.pack(pady=20)


e2=Entry(window,text='',font=("Ariel",24),bd=0,bg="systembuttonface")
e2.pack(padx=20,pady=20)


f=Frame(window)
f.pack(pady=20)
b=Button(f,text="Generate Password",command=new_rand)
b.pack()


window.mainloop()
