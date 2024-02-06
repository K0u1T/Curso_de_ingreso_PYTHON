import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Martin
apellido: Alvarez
---
Ejercicio: entrada_salida_02
---
Enunciado:
Al presionar el botón  'Mostrar', se deberá obtener un dato utilizando el Dialog Prompt
y luego mostrarlo utilizando el Dialog Alert
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()
        
        self.title("UTN FRA")
       
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        primer_dato_ingresado = prompt(None , 'Ingrese un dato')
        segundo_dato_ingresado = prompt(None, 'Ingrese otro dato')
        mesaje= None
        mensaje = f"El dato que se ingreso es: {primer_dato_ingresado}, y el segundo dato es {segundo_dato_ingresado}"
        alert('Ejercicio 02' , mensaje)
    
        
        
        # EJEMPLOS DE CONCATENACION
        # alert('Ejercicio 02' , 'El dato ingresado es -> ' + dato_ingresado)
        # alert('Ejercicio 02' , f"el dato que se ingreso es: {dato_ingresado}"")
        
        # alert('Ejercicio 02', 'El primer dato ingresados es: {0}, el segundo dato ingresado es: {1}', format(dato1, segundo_dato_ingresado))
        
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()