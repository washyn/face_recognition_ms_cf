# el usuario abre el programa
# ingresa los datos
# da click en guardar
# mensaje con los datos a guardar,
# se guarda los datos
# se abre la webcam, para tomar imagenes
# se toma imagenes, se guarda en una carpeta
# se muestra ok images
# se cierra

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


import sqlite3
import os                                                  
import uuid



class Form(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Registro de persona")

        self.resizable(False, False)
        
        self.nombres = None
        self.apellidos = None
        self.codigo = None


    def create_all_controls(self):
        label = ttk.Label (self, text="Formulario de registro")        
        label.grid(pady=(0,10),padx=(5,0),row = 0)

        label2 = ttk.Label (self, text="Nombres" )
        label2.grid(row = 1, column = 1)

        label3 = ttk.Label (self, text="Apellidos" )
        label3.grid(row = 3, column = 1)

        label4 = ttk.Label (self, text="Codigo" )
        label4.grid(row = 4, column = 1)



        self.nombres = tk.StringVar()
        entry = ttk.Entry(self, textvariable = self.nombres)
        entry.grid(padx = (20,20), row = 1, column = 2)

        self.apellidos = tk.StringVar()
        entry2 = ttk.Entry(self, textvariable = self.apellidos)
        entry2.grid(padx = (20,20), row = 3, column = 2)

        self.codigo = tk.StringVar()
        entry3 = ttk.Entry(self, textvariable = self.codigo)
        entry3.grid(padx = (20,20), row = 4, column = 2)

        button = tk.Button(self, text="Guardar datos", command = self.mostrar_mensaje)
        button.grid(pady=(20,20),row = 5, column = 2)


    def mostrar_mensaje(self):
        messagebox.showinfo("Datos a guardar",f"Nombres : {self.nombres.get()}\nApellidos : {self.apellidos.get()}\nCódigo : {self.codigo.get()}")

        # newStudent = addStudent(f"{self.nombres.get()} {self.apellidos.get()}", f"{self.codigo.get()}")

        messagebox.showinfo("Registro de caras",f"Se procedera a realizar un registro de su cara, realize todos los gestos necesarios con su rostro para poder ser reconocido porteriormente.")
        # create folders
        # folder = createStudentImagesFolder(newStudent.folderGuid)
        # register
        # creaateSampleFacesStudent(folder)

        messagebox.showinfo("Terminado de procesar","Se termino de registrar el estudiante")
        

        self.nombres.set("")
        self.codigo.set("")
        self.apellidos.set("")


        # close window
        # self.quit()


if __name__ == "__main__":
    tc = Form()
    tc.create_all_controls()
    tc.mainloop()



