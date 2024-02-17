import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


'''
nombre: Martin
apellido: Alvarez
---
Ejercicio: while_02bis
---
Enunciado:
Al presionar el botón ‘Mostrar Iteración’, mostrar mediante alert la suma 
de los numeros pares comprendidos entre el 1 y el 10.
'''


class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        self.btn_mostrar_iteracion = customtkinter.CTkButton(master=self, text="Mostrar iteración", command=self.btn_mostrar_iteracion_on_click)
        self.btn_mostrar_iteracion.grid(row=2, pady=20, columnspan=2, sticky="nsew")
        
    
    def btn_mostrar_iteracion_on_click(self):
        contador = 0 #contador
        suma_numeros_pares = 0 #acumulador de numeros que sean pares (en es caso)

        while(contador < 10):
            contador = contador + 1
            resto = contador % 2 #si el resultado es 0, esttoyy ante un numero par, de lo contrario es impar

            if(resto == 0): #esto determina si el numero almacenado en contador es par o impar
                #suma de pares
                suma_numeros_pares = suma_numeros_pares + contador

        alert("" , suma_numeros_pares)

            #contador += 2
            #alert("", contador)


    
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()