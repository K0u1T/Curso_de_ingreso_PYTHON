import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Martin
apellido: Alvarez
---
Ejercicio: if_05
---
Enunciado:
Al presionar el botón 'Calcular', se deberá obtener el contenido de la caja de texto txtEdad, 
transformarlo en número e informar si la persona "NO ES ADOLESCENTE" utilizando el Dialog Alert.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.label1 = customtkinter.CTkLabel(master=self, text="Edad")
        self.label1.grid(row=0, column=0, padx=20, pady=10)
        
        self.txt_edad = customtkinter.CTkEntry(master=self)
        self.txt_edad.grid(row=0, column=1)
                
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        edad_str = self.txt_edad.get()
        edad_num = int(edad_str)

        if(edad_num  > 18 or edad_num < 13 ):
            alert("tittle" , "No es ADOLESCENTE")

    # TABLA DE VERDAD #

# OR	*********************
# Cond1	Cond2	Resultado
# TRUE	TRUE	TRUE
# FALSE	TRUE	TRUE
# TRUE	FALSE	TRUE
# FALSE	FALSE	FALSE

# AND ***********************
# Cond1	C#ond2	Resultado
# TRUE	TRUE	TRUE
# FALSE	TRUE	FALSE
# TRUE	FALSE	FALSE
# FALSE	FALSE	FALSE
# NOT ********************
# Cond1		Resultado
# TRUE		FALSE
# FALSE		TRUE
        
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()