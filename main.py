from tkinter import *
from tkinter.ttk import *

from time import strftime

root = Tk()
root.title("Clock made by @CaidnAnimates")

def time():
    string = strftime('%I:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)

label = Label(root, font=("ds-digital", 80), background = "black", foreground = "cyan")
label.pack(anchor='center')
time()

mainloop()

#if you want to change this from a 24 hour clock to a 12 hour clock, just change the "H" in  (%H:%M:%S %p) to an "I"
