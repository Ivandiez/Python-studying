from tkinter import *

class Block:
    def __init__(self, master):
        self.e = Entry(master, width=20)
        self.b = Button(master, text="Преобразовать")
        self.l = Label(master, bg="black", fg="white", width=20)
        self.b["command"] = self.str_to_sort_list
        self.e.pack()
        self.b.pack()
        self.l.pack()

    # преобразует строку в исполняемый код
    def set_func(self, func):
        self.b['command'] = eval('self.' + func)
    
    def str_to_sort_list(self):
        s = self.e.get()
        s = s.split()
        s.sort()
        self.l["text"] = " ".join(s)

    def str_reverse(self):
        s = self.e.get()
        s = s.split()
        s.reverse()
        self.l['text'] = ' '.join(s)

root = Tk()

first_block = Block(root)
first_block.set_func("str_to_sort_list")

second_block = Block(root)
second_block.set_func("str_reverse")

root.mainloop()
