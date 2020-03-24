#tkinter=module และปรับย่อโดย tk
import tkinter as tk
import tkinter as ttk
from tkinter.ttk import Combobox

#Tk=Class#win=instance Variableชี้ไปยัง Class Tk
win=tk.Tk()
win.title("Python GUI")

#Label = Class
a_label=ttk.Label(win,text="Enter a name:")
a_label.grid(column=0,row=0)

def click_me():
    action.config(text="Hello "+ name.get()+' '+number.get())

#add button
action=ttk.Button(win,text="Click Me!",command=click_me)
action.grid(column=2,row=1)

#add a Text box
name=tk.StringVar()
name_entered=ttk.Entry(win,width=12,textvariable=name)
name_entered.grid(column=0,row=1)
name_entered.focus()

#add combobox
ttk.Label(win,text='Choose a number').grid(column=1,row=0)
number=tk.StringVar()
number_chosen=Combobox(win,width=12,textvariable=number)
number_chosen['values']=(0,1,2,3)
number_chosen.grid(column=1,row=1)
number_chosen.current(0)
#Window Open
win.mainloop()
