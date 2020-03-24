#tkinter=module และปรับย่อโดย tk
import tkinter as tk
import tkinter as ttk
#Tk=Class#win=instance Variableชี้ไปยัง Class Tk
win=tk.Tk()
win.title("Python GUI")

#Label = Class
a_label=ttk.Label(win,text="A Label")
a_label.grid(column=0,row=0)

def click_me():
    action.config(text="**I have been Clicked!**")
    a_label.config(foreground='red')
    a_label.config(text='A Red Label')

action=ttk.Button(win,text="Click Me!",command=click_me)
action.grid(column=1,row=0)

win.mainloop()