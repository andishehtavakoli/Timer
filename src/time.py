from tkinter import *
from tkinter.ttk import *
import time

root=Tk()

root.title('Clock')
label = Label(root, background='black', foreground='black')

def time_1():
    time_=time.strftime("%H:%M:%S")
    label.config(text=time_)
    label.after(1000,time_1)
    
label.pack()
time_1()

mainloop()