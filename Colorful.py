from tkinter import *

root = Tk()

colors = {
    "красный": "#ff0000",
    "оранжевый":"#ff7d00",
    "желтый":"#ffff00",
    "зеленый":"#00ff00",
    "голубой":"#007dff",
    "синий":"#0000ff",
    "фиолетовый":"#7d00ff"
}

class Butn:
    def __init__(self, master, color, code_color):
        self.color = color
        self.code_color = code_color
        self.b = Button(master, width=13, bg=self.code_color, command=self.set_color)
        self.b.pack()

    def set_color(self):
        l.config(text=self.color)
        e.delete(0, END)
        e.insert(0, self.code_color)

l = Label(root)
e = Entry(root, justify="center", bd=5)

l.pack()
e.pack()

for col in colors.keys():
    Butn(root, col, colors[col])
    
root.mainloop()
