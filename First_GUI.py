#tkinter=module และปรับย่อโดย tk
import tkinter as tk

#Tk=Class#win=instance Variableชี้ไปยัง Class Tk
win=tk.Tk()
win.title("Python GUI")
#resizable is method of Tk()
win.resizable(False,False)
win.mainloop()