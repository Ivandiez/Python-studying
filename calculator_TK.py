from tkinter import *

class Calculation:
    def __init__(self, master):
        self.e1 = Entry(master, width=20)
        self.e2 = Entry(master, width=20)
        
        self.b1 = Button(master, text="+")
        self.b2 = Button(master, text="-")
        self.b3 = Button(master, text="*")
        self.b4 = Button(master, text="/")

        self.l = Label(master, bg="black", fg="white", width=20)

        self.b1['command'] = self.add
        self.b2['command'] = self.subtract
        self.b3['command'] = self.multiply
        self.b4['command'] = self.divide

        self.e1.pack()
        self.e2.pack()
        self.b1.pack()
        self.b2.pack()
        self.b3.pack()
        self.b4.pack()
        self.l.pack()
        
    def add(self):
        try:
            self.l['text'] = float(self.e1.get()) + float(self.e2.get())
        except:
            self.l['text'] = "Error!"

    def subtract(self):
        try:
            self.l['text'] = float(self.e1.get()) - float(self.e2.get())
        except:
            self.l['text'] = "Error!"

    def multiply(self):
        try:
            self.l['text'] = float(self.e1.get()) * float(self.e2.get())
        except:
            self.l['text'] = "Error!"

    def divide(self):
        try:
            self.l['text'] = float(self.e1.get()) / float(self.e2.get())
        except:
            self.l['text'] = "Error!"

root = Tk()

res = Calculation(root)

root.mainloop()
