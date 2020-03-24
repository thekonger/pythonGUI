#tkinter=module และปรับย่อโดย tk
import tkinter as tk
import tkinter as ttk
from tkinter import scrolledtext
from tkinter.ttk import Combobox

#Tk=Class#win=instance Variableชี้ไปยัง Class Tk
win=tk.Tk()
win.title("Python GUI")

#Label = Class
a_label=ttk.Label(win,text="Enter a name:")
a_label.grid(column=0,row=0)

def click_me():
    action.config(text="Hello "+ name.get()+' '+number.get())
def radCall():
    radSel=radVar.get()
    if radSel==1:win.config(background=COLOR1)
    elif radSel==2:win.config(background=COLOR2)
    elif radSel ==3:win.config(background=COLOR3)
    print(radSel)
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
number_chosen['values']=(0,1,2,4,42,100)
number_chosen.grid(column=1,row=1)
number_chosen.current(0)

#add radiobutton
COLOR1='Blue'
COLOR2='Gold'
COLOR3='Red'
radVar=tk.IntVar()
rad1=tk.Radiobutton(win,text=COLOR1,variable=radVar,value=1,command=radCall)
rad1.grid(column=0,row=5,sticky=tk.W,columnspan=3)

rad2=tk.Radiobutton(win,text=COLOR2,variable=radVar,value=2,command=radCall)
rad2.grid(column=1,row=5,sticky=tk.W,columnspan=3)

rad3=tk.Radiobutton(win,text=COLOR3,variable=radVar,value=3,command=radCall)
rad3.grid(column=2,row=5,sticky=tk.W,columnspan=3)

#add Scrolled Text control
scrol_w=30
scrol_h=3
scr=scrolledtext.ScrolledText(win,width=scrol_w,height=scrol_h,wrap=tk.WORD)
scr.grid(column=0,columnspan=100)
#Window Open
win.mainloop()
