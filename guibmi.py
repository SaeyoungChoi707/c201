from ctypes.wintypes import MSG
from tkinter import *
window = Tk()
window.title("SI CALCULATOR")
window.geometry("400x400")
window.configure(bg="lightblue")

headinglabel = Label(window,text="SI CALCULATOR",fg="black",bg="lightblue",font=("Calibri",20),bd=5)
headinglabel.place(x=50,y=20)

namelabel = Label(window,text="Enter Time",fg="black",bg="lightblue",font=("Calibri",12),bd=1)
namelabel.place(x=20,y=90)

username = Entry(window,text="",bd=2,width=22)
username.place(x=150,y=92)

heightlabel = Label(window,text="Enter Principal",fg="black",bg="lightblue",font=("Calibri",12))
heightlabel.place(x=20,y=140)

heightentry = Entry(window,text="",bd=2,width=15)
heightentry.place(x=150,y=142)

weightlabel = Label(window,text="Enter Rate",fg="black",bg="lightblue",font=("Calibri",12))
weightlabel.place(x=20,y=185)

weightentry = Entry(window,text="",bd=2,width=15)
weightentry.place(x=150,y=187)

def calculate_bmi():
    r=float(weightentry.get())
    p=float(heightentry.get())
    t=float(username.get())
    si=p*r*t/100
    
    resultlabel.destroy()
    
    outputmsg = Label(resultframe,text="Your Interest is "+str(si),fg="black",bg="lightblue",font=("Calibri",12),width=42)
    outputmsg.place(x=20,y=40)
    outputmsg.pack()

calculatebutton = Button(window,text="Calculate",fg="white",bg="blue",bd=4,command=calculate_bmi)
calculatebutton.place(x=20,y=250)

resultframe = LabelFrame(window,text="Result",bg="lightblue",font=("Calibri",12))
resultframe.pack(padx=20,pady=20)
resultframe.place(x=20,y=300)

resultlabel = Label(resultframe,text=" ",bg="lightblue",font=("Calibri",12),width=33)
resultlabel.place(x=20,y=20)
resultlabel.pack()

window.mainloop()