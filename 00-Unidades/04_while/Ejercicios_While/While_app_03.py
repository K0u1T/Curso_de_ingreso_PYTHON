import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


'''
nombre: Martin
apellido: Alvarez
---
Ejercicio: while_03
---
Enunciado:
Al presionar el botón ‘Pedir clave’, solicitar al usuario que ingrese una contraseña mediante prompt. 
Comprobar que la contraseña ingresada sea ‘utn750’. En caso de no coincidir, volver a solicitarla hasta que coincidan.
'''


class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        self.btn_pedir_clave = customtkinter.CTkButton(master=self, text="Ingresar", command=self.btn_pedir_clave_on_click)
        self.btn_pedir_clave.grid(row=2, pady=20, columnspan=2, sticky="nsew")
        
    
    def btn_pedir_clave_on_click(self):
        clave = prompt("Ingresar" , "Ingrese la clave. La clave es: utn750")

        while(clave != "utn750"):
           clave = prompt("Error" , "No es la clave correcta")


        #datos validos para ingresar al sistema
        #usuario_valido = "admin"
        #clave_valida = "12345"

        #datos ingresados por el usuario
        #usuario = prompt("ingreso" , "ingrese su usuario")
        #clave = prompt ("ingrese" , "ingrese su clave")

        #while(usuario != usuario_valido or clave != clave_valida):
            #usuario = prompt("Error" , "Re-ingrese su usuario")
            #clave = prompt("Error" , "Re-ingrese su clave")

        #alert("Bienvenido" , f"Bienvenido {usuario}")
        


    
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()