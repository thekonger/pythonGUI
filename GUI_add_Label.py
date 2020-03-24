#tkinter=module และปรับย่อโดย tk
import tkinter as tk
import tkinter as ttk
#Tk=Class#win=instance Variableชี้ไปยัง Class Tk
win=tk.Tk()
win.title("Python GUI")

#Label = Class
a_label=ttk.Label(win,text="A Label")
a_label.grid(column=0,row=0)

win.mainloop()