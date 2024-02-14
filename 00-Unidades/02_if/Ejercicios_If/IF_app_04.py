import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Martin
apellido: Alvarez
---
Ejercicio: if_04
---
Enunciado:
Al presionar el botón 'Calcular', se deberá obtener el contenido de la caja de texto txtEdad, 
transformarlo en número y calcular si es adolescente (edad entre 13 y 17 años). Se deberá informar utilizando el Dialog alert.
'''


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.label1 = customtkinter.CTkLabel(master=self, text="Edad")
        self.label1.grid(row=0, column=0, padx=20, pady=10)

        self.txt_edad = customtkinter.CTkEntry(master=self)
        self.txt_edad.grid(row=0, column=1)

        self.btn_mostrar = customtkinter.CTkButton(
            master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")

    def btn_mostrar_on_click(self):
        edad = self.txt_edad.get()
        edad_num = int(edad)

        if(edad_num > 12):

            if(edad_num < 18):
               alert("tittle" , "Es ADOLESCENTE")



        # edad = self.txt_edad.get()
        # edad = int(edad)
        # nombre = prompt = ("ingrese" , "su nombre es: ")
               

        # if(edad > 17):
              #estado = "mayor"

        # elif(edad > 12):
               #estado = "adolescente"

        # else:
               #estado = "niño"


        # alert("su edad" , estado)  


        # if nombre maria
               #if




        # if (nombre == "María and edad > 17"):
               #if (edad) > 17
                    #estado = "Mayor"
        # elif (nombre != "Maria" and edad> 17)
               #estado = "Maria no es mayor"
        # elif (nombre == "maria" and edad > 12)

        ## No hacer if innecesarios (if son como preguntas de SI tiene) porque satura el procesador ##
       

          
        # else:
            # alert("su dad" , "no tiene 18")
                    
        

       ## REPASO ENTRADA Y SALIDA ## 
    # salida
    # alert("sabados" , "bienvenidos")

    # self.txt_edad.delete(0 , 200)
    # self.txt_edad.insert(0 , "Hola")
    
    # entrada
    # nombre = prompt("su nombre" , "Ingrese su nombre")
    # edad = self.txt_edad.get()

    # castear
    # edad_texto = self.txt_edad.get()
    # edad_num = int(edad_texto)


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()