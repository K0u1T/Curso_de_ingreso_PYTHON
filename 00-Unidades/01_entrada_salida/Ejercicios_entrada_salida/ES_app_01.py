import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter
import math

'''''
nombre: martin 
apellido: alvarez
---
Ejercicio: entrada_salida_01
---
Enunciado:
La juguetería El MUNDO DE OCTAVIO nos encarga un programa para conocer qué cantidad de materiales se necesita para la fabricación de distintos juguetes.

AB = Diágonal mayor
DC = Diágonal menor
BD y BC = lados menores
AD y AC = lados mayores

Debemos tener en cuenta que la estructura del cometa estará dada por un perímetro de varillas de plástico y los correspondientes entrecruces (DC y AB) del mismo material para mantener la forma del cometa.
El cometa estará construido con papel de alta resistencia. La cola del mismo se construirá con el mismo papel que el cuerpo y representará un 10% adicional del necesario para el cuerpo.
Necesitamos saber cuántos Mts de varillas de plástico y cuántos de papel son necesarios para la construcción en masa de 10 cometas. Tener en cuenta que los valores de entrada están expresados en Cms.

Ahora necesitamos saber cuánto papel de cada color necesitamos. Las entradas son las mismas.

'''

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.btn_mostrar = customtkinter.CTkButton(
            master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")

    #def btn_mostrar_on_click(self):
        #alert(title= "UTN" , message = "Esto no anda, funciona")

    
    #def btn_mostrar_on_click(self):
        #dolar_oficial = prompt("Ingrese" , "Dolar Oficial") 
        #dolar_blue = prompt("Ingrese" , "Dolar Blue")

        #dolar_oficial = float(dolar_oficial)
        #dolar_blue = float(dolar_blue)

        #porcentaje_dolar_of = 100

        #porcentaje_dolar_b = (dolar_blue * porcentaje_dolar_of) / dolar_oficial
        #diferencia_porcentaje = porcentaje_dolar_b - porcentaje_dolar_of

        #mensaje = f"La diferencia entre el dolar oficial y el dolar blue es de: {diferencia_porcentaje:.2f} %, el dolar blue es más caro"
        
        #alert("Mensaje" , mensaje)

    

    #def btn_mostrar_on_click(self):
        #PRECIO_X_KILO_PASAJERO = 1000

        #nombre_pasajero_1 = prompt("Ingrese" , "Ingrese el nombre del 1er pasajero")
        #nombre_pasajero_2 = prompt("Ingrese" , "Ingrese el nombre del 2do pasajero")

        #edad_pasajero_1 = prompt("Ingrese" , "Ingrese la edad del 1er pasajero ")
        #edad_pasajero_2 = prompt("Ingrese" , "Ingrese la edad del 2do pasajero ")
        #edad_pasajero_1 = int(edad_pasajero_1)
        #edad_pasajero_2 = int(edad_pasajero_2)


        #peso_pasajero_1 = prompt("Ingrese" , "Ingrese el peso del 1er pasajero")
        #peso_pasajero_2 = prompt("Ingrese" , "Ingrese el peso del 2do pasajero")
        #peso_pasajero_1 = float(peso_pasajero_1)
        #peso_pasajero_2 = float(peso_pasajero_2)

        #suma_peso = float(peso_pasajero_1 + peso_pasajero_2)
        #edad_promedio = int(edad_pasajero_1 + edad_pasajero_2) / 2
        #precio_total_viaje = suma_peso * PRECIO_X_KILO_PASAJERO

        #mensaje = f"Hola {nombre_pasajero_1} y {nombre_pasajero_2}, su edad promedio es {edad_promedio} , y su peso es de {peso_pasajero_1:.2f} kg y {peso_pasajero_2} respectivamente, sumado dan {suma_peso:.2f} kg, y su viaje vale {precio_total_viaje:.2f} $ "

        #alert("Mensaje" , mensaje)
        
    def btn_mostrar_on_click(self):
        #definir los datos por prompt y su valor numerico
        diagonal_mayor = prompt("Ingrese los datos" , "Diagonal mayor")
        diagonal_mayor = float(diagonal_mayor)

        diagonal_menor = prompt("Ingrese los datos" , "Diagonal menor")
        diagonal_menor = float(diagonal_menor)

        lado_menor = prompt("Ingrese los datos" , "Lados menores")
        lado_menor = float(lado_menor)
        
        lado_mayor = prompt("Ingrese los datos" , "Lados mayores")
        lado_mayor = float(lado_mayor)

        #Es la cuenta de los 4 lados "bd" , "bc" , "ad" , "ac"
        primer_perimetro = (lado_mayor + lado_menor) * 2 

        segundo_perimetro = diagonal_mayor + diagonal_menor

        resultado_perimetro = primer_perimetro + segundo_perimetro

        #area del papel
        area = (diagonal_mayor * diagonal_menor) / 2

        cola_cometa = area * 0.1

        total_perimetro = (resultado_perimetro / 100) * 10

        papel_cometa = area + cola_cometa

        total_papel_cometa = (papel_cometa / 100) *10

        alert("MUNDO OCTAVIO" , f"Necesitas {math.ceil(total_perimetro)} Metros de varillas,"
            f" {math.ceil(total_papel_cometa)} Metros2 de cada color de papel para 10 cometas")
    
    
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
