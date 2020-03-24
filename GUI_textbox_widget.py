#tkinter=module และปรับย่อโดย tk
import tkinter as tk
import tkinter as ttk
#Tk=Class#win=instance Variableชี้ไปยัง Class Tk
win=tk.Tk()
win.title("Python GUI")

#Label = Class
a_label=ttk.Label(win,text="Enter a name:")
a_label.grid(column=0,row=0)

def click_me():
    action.config(text="Hello "+ name.get())

#add button
action=ttk.Button(win,text="Click Me!",command=click_me)
action.grid(column=1,row=1)
action.config(state='disabled')
#add a Text box
name=tk.StringVar()
name_entered=ttk.Entry(win,width=12,textvariable=name)
name_entered.grid(column=0,row=1)
name_entered.focus()
win.mainloop()