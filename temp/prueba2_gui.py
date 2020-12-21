from tkinter import *

from tkinter import messagebox

from tkinter import ttk
####################################################################
# Todos:
# add labels 
# add entrys
# add buttons
# add functions
# lo mas basico posible

####################################################################



class MyWindow:
    def __init__(self, win):

        self.aa = Label(win ,text = "Nombres").grid(row = 0,column = 0)
        self.bb = Label(win ,text = "Apellidos").grid(row = 1,column = 0)
        self.cc = Label(win ,text = "Código").grid(row = 2,column = 0)

        self.entry1 = Entry(win, state = "disabled").grid(row = 0,column = 1)
        self.entry2 = Entry(win, state = "disabled").grid(row = 1,column = 1)
        self.entry3 = Entry(win, state = "disabled").grid(row = 2,column = 1)

        self.btn1 = ttk.Button(win ,text="Registrar", command = self.add).grid(row=4,column=0)
        self.btn2 = ttk.Button(win ,text="Guardar").grid(row=4,column=1)
        self.btn3 = ttk.Button(win ,text="Salir", command = win.quit).grid(row=4,column=2)




        # self.lbl1=Label(win, text='First number')
        # self.lbl2=Label(win, text='Second number')
        # self.lbl3=Label(win, text='Result')

        # self.t1=Entry(bd=3)
        # self.t2=Entry()
        # self.t3=Entry()

        # self.btn1 = Button(win, text='Add')
        # self.btn2=Button(win, text='Subtract')

        # self.lbl1.place(x=100, y=50)
        # self.t1.place(x=200, y=50)
        # self.lbl2.place(x=100, y=100)
        # self.t2.place(x=200, y=100)
        # self.b1=Button(win, text='Add', command=self.add)
        # self.b2=Button(win, text='Subtract')
        # self.b2.bind('<Button-1>', self.sub)
        # self.b1.place(x=100, y=150)
        # self.b2.place(x=200, y=150)
        # self.lbl3.place(x=100, y=200)
        # self.t3.place(x=200, y=200)


    def add(self):
        # tkinter.messagebox.showinfo(title="None", message="None")
        # messagebox.showinfo(message="Mensaje", title="Título")
        print(self.entry1)
        # self.entry1.configure(state="normal")
        # self.entry1["state"] = "normal"
        print(self.entry1["state"])
        # self.a1["state"] = "normal"
        # messagebox.showinfo(message="Mensaje", title="Título")

        self.t3.delete(0, 'end')
        num1=int(self.t1.get())
        num2=int(self.t2.get())
        result=num1+num2
        self.t3.insert(END, str(result))

    def sub(self, event):
        self.t3.delete(0, 'end')
        num1=int(self.t1.get())
        num2=int(self.t2.get())
        result=num1-num2
        self.t3.insert(END, str(result))




window=Tk()
mywin=MyWindow(window)
window.title("Registro de estudiante")
# window.geometry("400x300+10+10")
window.geometry("280x400")
window.mainloop()



