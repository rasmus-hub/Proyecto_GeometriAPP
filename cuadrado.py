# Ventana de la figura del cuadrado para mostrar sus resultados y dibujos graficamente en la UI

""" NOTA: Cada comentario de este archivo se replica en los otros, por lo tanto para ahorrar líneas de código en todos, 
no se han incluido en los demás, solo en este como ejemplo """

# Importamos los módulos necesarios
import tkinter as tk
from tkinter import messagebox
from calculo import calcular_area_perimetro_cuadrado

# Definimos una función para mostrar la ventana del cuadrado
def mostrar_ventana_cuadrado(ventana_principal):
    ventana_cuadrado = tk.Toplevel(ventana_principal) # Creamos una ventana secundaria a partir de la ventana principal
    ventana_cuadrado.title("Cuadrado") # Le damos un título a la ventana

    tk.Label(ventana_cuadrado, text="Lado del cuadrado:").pack() # Creamos una etiqueta para pedir el lado del cuadrado

    entry_lado_cuadrado = tk.Entry(ventana_cuadrado) # Creamos una entrada de texto para recibir el lado del cuadrado
    entry_lado_cuadrado.pack()

    # Definimos una función para calcular el área y el perímetro del cuadrado
    def calcular_cuadrado():
        # Usamos un bloque try-except para manejar posibles errores
        try:
            lado = float(entry_lado_cuadrado.get()) # Obtenemos el valor del lado del cuadrado como un número real
            if lado <= 0: # Verificamos que el lado sea positivo
                messagebox.showerror("Error", "Por favor, no ingrese números negativos.") # Si no lo es, mostramos un mensaje de error
            else:
                area, perimetro = calcular_area_perimetro_cuadrado(lado) # Si lo es, llamamos a la función del módulo calculo para obtener el área y el perímetro mostrando los resultados
                messagebox.showinfo(title='Resultados', message=f"Área: {round(area, 3)}\nPerímetro: {round(perimetro, 3)}") 
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese un número válido.") # Si el valor ingresado anteriormente no es un número válido, mostramos un mensaje de error
    
    # Definimos una función para dibujar el cuadrado en un canvas
    def dibujar_cuadrado():
        # Usamos un bloque try-except para manejar posibles errores
        try:
            # Obtenemos el valor del lado del cuadrado como un número real
            lado = float(entry_lado_cuadrado.get())
            # Verificamos que el lado sea positivo
            if lado <= 0:
                # Si no lo es, mostramos un mensaje de error
                messagebox.showerror("Error", "Por favor, no ingrese números negativos.")
            else:
                # Si lo es, creamos una ventana y un canvas para dibujar el cuadrado
                root = tk.Tk()
                canvas = tk.Canvas(root, width=400, height=400, bg="white")
                canvas.pack()
                # Calculamos el centro del canvas
                x, y = canvas.winfo_reqwidth() / 2, canvas.winfo_reqheight() / 2
                # Dibujamos el cuadrado con el lado dado, centrado en el canvas y de color azul
                canvas.create_rectangle(x - lado / 2, y - lado / 2, x + lado / 2, y + lado / 2, fill="blue")
                # Mostramos la medida del lado en la parte inferior del cuadrado
                medida_lado = canvas.create_text((x - lado / 2), (y + lado / 2) + 5, anchor='nw')
                canvas.itemconfig(medida_lado, text=lado)
                canvas.insert(medida_lado, 12, 'cm')
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese números válidos.") # Si el valor ingresado no es un número válido, mostramos un mensaje de error

    # Creamos un botón para llamar a la función de calcular el cuadrado
    btn_calcular_cuadrado = tk.Button(ventana_cuadrado, text="Calcular", command=calcular_cuadrado)
    btn_calcular_cuadrado.pack()

    # Creamos un botón para llamar a la función de dibujar el cuadrado
    btn_dibujar_cuadrado = tk.Button(ventana_cuadrado, text='Dibujar Cuadrado', command=dibujar_cuadrado)
    btn_dibujar_cuadrado.pack()
