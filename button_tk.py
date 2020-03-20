from tkinter import *

root = Tk()
b1 = Button(text="Изменить", width=15, height=3)

def change():
    b1['text'] = "Изменено"
    b1['bg'] = '#000000'  # цвет фона
    b1['activebackground'] = '#555555' # цвет фона во время нажатия
    b1['fg'] = '#ffffff' # цвет текста
    b1['activeforeground'] = '#ffffff' # цвет текста во время нажатия

b1.config(command=change) # установка свойства command

b1.pack()
root.mainloop()
