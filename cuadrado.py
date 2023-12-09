# Ventana de la figura del cuadrado para mostrar sus resultados y dibujos graficamente en la UI

import tkinter as tk
from tkinter import messagebox
from calculo import calcular_area_perimetro_cuadrado

def mostrar_ventana_cuadrado(ventana_principal):
    ventana_cuadrado = tk.Toplevel(ventana_principal)
    ventana_cuadrado.title("Cuadrado")

    tk.Label(ventana_cuadrado, text="Lado del cuadrado:").pack()
    entry_lado_cuadrado = tk.Entry(ventana_cuadrado)
    entry_lado_cuadrado.pack()

    def calcular_cuadrado():
        try:
            lado = float(entry_lado_cuadrado.get())
            if lado <= 0:
                messagebox.showerror("Error", "Por favor, no ingrese números negativos.")
            else:
                area, perimetro = calcular_area_perimetro_cuadrado(lado)
                messagebox.showinfo(title='Resultados', message=f"Área: {round(area, 3)}\nPerímetro: {round(perimetro, 3)}")
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese un número válido.")
    
    def dibujar_cuadrado():
        try:
            lado = float(entry_lado_cuadrado.get())

            if lado <= 0:
                messagebox.showerror("Error", "Por favor, no ingrese números negativos.")
            else:
                root = tk.Tk()
                canvas = tk.Canvas(root, width=400, height=400, bg="white")
                canvas.pack()
                x, y = canvas.winfo_reqwidth() / 2, canvas.winfo_reqheight() / 2
                canvas.create_rectangle(x - lado / 2, y - lado / 2, x + lado / 2, y + lado / 2, fill="blue")

                medida_lado = canvas.create_text((x - lado / 2), (y + lado / 2) + 5, anchor='nw')
                canvas.itemconfig(medida_lado, text=lado)
                canvas.insert(medida_lado, 12, 'cm')
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese números válidos.")

    btn_calcular_cuadrado = tk.Button(ventana_cuadrado, text="Calcular", command=calcular_cuadrado)
    btn_calcular_cuadrado.pack()

    btn_dibujar_cuadrado = tk.Button(ventana_cuadrado, text='Dibujar Cuadrado', command=dibujar_cuadrado)
    btn_dibujar_cuadrado.pack()