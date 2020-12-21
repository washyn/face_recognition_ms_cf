
# ESTO PRIMERO
# interfaz con controlles basicos, 
# registrar y se activa la camara
# y message de terminado de registrar
# se limpia controlles y release de camara



# from tkinter import *
# fields = ('Annual Rate', 'Number of Payments', 'Loan Principle', 'Monthly Payment', 'Remaining Loan')

# def monthly_payment(entries):
#     # period rate:
#     r = (float(entries['Annual Rate'].get()) / 100) / 12
#     print("r", r)
#     # principal loan:
#     loan = float(entries['Loan Principle'].get())
#     n = float(entries['Number of Payments'].get())
#     remaining_loan = float(entries['Remaining Loan'].get())
#     q = (1 + r)** n
#     monthly = r * ( (q * loan - remaining_loan) / ( q - 1 ))
#     monthly = ("%8.2f" % monthly).strip()
#     entries['Monthly Payment'].delete(0,END)
#     entries['Monthly Payment'].insert(0, monthly )
#     print("Monthly Payment: %f" % float(monthly))

# def final_balance(entries):
#     # period rate:
#     r = (float(entries['Annual Rate'].get()) / 100) / 12
#     print("r", r)
#     # principal loan:
#     loan = float(entries['Loan Principle'].get())
#     n = float(entries['Number of Payments'].get())
#     q = (1 + r)** n
#     monthly = float(entries['Monthly Payment'].get())
#     q = (1 + r)** n
#     remaining = q * loan - ( (q - 1) / r) * monthly
#     remaining = ("%8.2f" % remaining).strip()
#     entries['Remaining Loan'].delete(0,END)
#     entries['Remaining Loan'].insert(0, remaining )
#     print("Remaining Loan: %f" % float(remaining))


# def makeform(root, fields):
#     entries = {}
#     for field in fields:
#         row = Frame(root)
#         lab = Label(row, width=22, text=field+": ", anchor='w')
#         ent = Entry(row)
#         ent.insert(0,"0")
#         row.pack(side = TOP, fill = X, padx = 5 , pady = 5)
#         lab.pack(side = LEFT)
#         ent.pack(side = RIGHT, expand = YES, fill = X)
#         entries[field] = ent
#     return entries

# if __name__ == '__main__':
#     root = Tk()
#     ents = makeform(root, fields)

#     root.bind('<Return>', (lambda event, e = ents: fetch(e)))

#     b1 = Button(root, text = 'Final Balance',
#         command=(lambda e = ents: final_balance(e)))
#     b1.pack(side = LEFT, padx = 5, pady = 5)

#     b2 = Button(root, text='Monthly Payment',
#     command=(lambda e = ents: monthly_payment(e)))
#     b2.pack(side = LEFT, padx = 5, pady = 5)

#     b3 = Button(root, text = 'Quit', command = root.quit)
#     b3.pack(side = LEFT, padx = 5, pady = 5)
#     root.mainloop()

########################################################

# from tkinter import *
# from tkinter import ttk

# window = Tk()
# window.title("Registro de estudiantes")
# window.geometry('280x400')
# # window.configure(background = "grey")

# aa = Label(window ,text = "Nombres").grid(row = 0,column = 0)
# bb = Label(window ,text = "Apellidos").grid(row = 1,column = 0)
# cc = Label(window ,text = "Código").grid(row = 2,column = 0)

# # c = Label(window ,text = "Email Id").grid(row = 2,column = 0)
# # d = Label(window ,text = "Contact Number").grid(row = 3,column = 0)

# a1 = Entry(window, state = "disabled").grid(row = 0,column = 1)
# b1 = Entry(window, state = "disabled").grid(row = 1,column = 1)
# c1 = Entry(window, state = "disabled").grid(row = 2,column = 1)

# # c1 = Entry(window).grid(row = 2,column = 1)
# # d1 = Entry(window).grid(row = 3,column = 1)

# # def clicked():
# #     res = "Welcome to " + txt.get()
# #     lbl.configure(text= res)


# def comandRegister():
#     a1.configure(state="normal")



# btn1 = ttk.Button(window ,text="Registrar", command = comandRegister).grid(row=4,column=0)
# btn2 = ttk.Button(window ,text="Guardar").grid(row=4,column=1)
# btn3 = ttk.Button(window ,text="Salir", command = window.quit).grid(row=4,column=2)

# # b3 = Button(root, text = 'Quit', command = root.quit)

# window.mainloop()


import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


def submit_0():
    messagebox.showinfo("Names",f"Name_0: {name0.get()}\nName_1: {name1.get()}\nName_2: {name2.get()}\n")

# def submit_1():
#     messagebox.showinfo("Values",f"Value_0: {value0.get()}\nValue_1: {value1.get()}\nValue_2: {value2.get()}\n")



class Form(tk.Tk):


    def __init__(self):
        super().__init__()
        self.title("Tkinter example without formatting")
        self.index = 0
        self.left_column, self.right_column = 1, 2
        self.value_radio = tk.IntVar()
        self.value_radio.set(2)


    " LABEL "

    def main_label(self, text):
        label = ttk.Label (self, text=text )
        label.grid(
            pady=(0,10),
            padx=(5,0),
            row = self.index
        )
        self.index += 1

    def param_label(self, text):
        label = ttk.Label (self, text=text )
        label.grid(
            row = self.index,
            column = self.left_column
        )
        self.index += 1


    " ENTRY "

    def input_field(self):
        value_entry = tk.StringVar()
        entry = ttk.Entry(self, textvariable = value_entry)
        entry.grid(
            padx = (20,20),
            row = self.index - 1,
            column = self.right_column
        )
        self.index += 1
        return value_entry


    " SPINBOX "

    def spin_box(self, set_spinbox):
        value_spinbox = tk.IntVar()
        value_spinbox.set(set_spinbox)
        spin = ttk.Spinbox (self,values=(1,2,3,4,5),textvariable=value_spinbox,state='readonly')
        spin.grid(
            row=self.index - 1,
            column=self.right_column
        )
        self.index += 1
        return value_spinbox


    " COMBOBOX "

    def combo_box(self, inputValues):
        value_combo = tk.StringVar()
        values = ttk.Combobox(self, textvariable=value_combo)
        values["values"] = (inputValues)
        values["state"] = "readonly"
        values.grid(
            row=self.index-1,
            column=self.right_column
        )
        self.index += 1
        return value_combo


    " RADIO BUTTON "

    def radio_button(self, text,value):
        radioButton = ttk.Radiobutton (self, text=text, variable=self.value_radio, value=value)
        radioButton.grid(
            row=self.index-1,
            column=self.right_column,
        )
        self.index += 1


    " NOTEBOOK -> TAB "

    def notebook(self, text):
        t = ttk.Notebook(self)
        tab1 = ttk.Frame(t)
        t.add(tab1, text=text)
        t.grid(
            pady = (0,10),
            row = 0,
            column = self.index
        )
        self.index += 1
        

    " BUTTON "

    def submit_button(self, submit):
        button = tk.Button(self, text="submit", command=submit)
        button.grid(pady=(20,20),row=self.index, column = 2)
        self.index += 1

    def create_all_controls(self):
        pass


if __name__ == "__main__":
    
    # combo_values = ["June","July","August"]

    tc = Form()
    
    # tc.notebook("Tab_1")
    # tc.notebook("Tab_2")

    tc.main_label("FORM_0")
    tc.param_label("Name_0:")

    name0 = tc.input_field()

    tc.param_label("Name_1:")

    name1 = tc.input_field()

    tc.param_label("Name_2:")

    name2 = tc.input_field()


    tc.submit_button(submit_0)




    # tc.main_label("FORM_1")
    # tc.param_label("Value_0:")

    # value0 = tc.spin_box(5)

    # tc.param_label("Value_1:")

    # value1 = tc.combo_box(combo_values)

    # tc.param_label("Value_2:")
    # tc.radio_button("A <- 1",1)
    # tc.radio_button("B <- 2",2)

    # value2 = tc.value_radio

    # tc.submit_button(submit_1)
    
    tc.mainloop()




