from tkinter import *

root = Tk()
l1 = Label(text="Machine learning", font="Arial 32")
l2 = Label(text="Pattern recognition", font=("Comic Sans MS", 24, "bold"))
l1.config(bd=20, bg='#ffaaaa') # bd - границы метки
l2.config(bd=20, bg='#aaffff')
l1.pack()
l2.pack()
root.mainloop()
