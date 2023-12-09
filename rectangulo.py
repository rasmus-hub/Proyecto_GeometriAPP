# Ventana de la figura del rectangulo para mostrar sus resultados y dibujos graficamente en la UI

import tkinter as tk
from tkinter import messagebox
from calculo import calcular_area_perimetro_rectangulo

def mostrar_ventana_rectangulo(ventana_principal):
    ventana_rectangulo = tk.Toplevel(ventana_principal)
    ventana_rectangulo.title("Rectángulo")

    tk.Label(ventana_rectangulo, text="Largo del rectangulo:").pack()
    entry_largo_rectangulo = tk.Entry(ventana_rectangulo)
    entry_largo_rectangulo.pack()

    tk.Label(ventana_rectangulo, text="Ancho del rectangulo:").pack()
    entry_ancho_rectangulo = tk.Entry(ventana_rectangulo)
    entry_ancho_rectangulo.pack()

    def calcular_rectangulo():
        try:
            largo = float(entry_largo_rectangulo.get())
            ancho = float(entry_ancho_rectangulo.get())
            if largo <= 0 or ancho <= 0:
                messagebox.showerror("Error", "Por favor, no ingrese números negativos.")
            else:
                area, perimetro = calcular_area_perimetro_rectangulo(largo, ancho)
                messagebox.showinfo(title='Resultados', message=f"Área: {round(area, 3)}\nPerímetro: {round(perimetro, 3)}")
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese números válidos.")
    
    def dibujar_rectangulo():
        try:
            largo, ancho = float(entry_largo_rectangulo.get()), float(entry_ancho_rectangulo.get())
            
            if largo <= 0 or ancho <= 0:
                messagebox.showerror("Error", "Por favor, no ingrese números negativos.")
            else:
                root = tk.Tk()
                canvas = tk.Canvas(root, width=400, height=400, bg="white")
                canvas.pack()
                x, y = canvas.winfo_reqwidth() / 2, canvas.winfo_reqheight() / 2
                canvas.create_rectangle(x - largo / 2, y - ancho / 2, x + largo / 2, y + ancho / 2, fill="blue", outline='black')

                medida_largo = canvas.create_text(x - largo / 2, (y - ancho / 2) - 5, anchor='sw')
                canvas.itemconfig(medida_largo, text=largo)
                canvas.insert(medida_largo, 12, 'cm')

                medida_ancho = canvas.create_text((x + largo / 2) + 5, y + ancho / 2, anchor='nw', angle=90)
                canvas.itemconfig(medida_ancho, text=ancho)
                canvas.insert(medida_ancho, 12, 'cm')
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese números válidos.")

    btn_calcular_rectangulo = tk.Button(ventana_rectangulo, text="Calcular", command=calcular_rectangulo)
    btn_calcular_rectangulo.pack()

    btn_dibujar_rectangulo = tk.Button(ventana_rectangulo, text="Dibujar Rectangulo", command=dibujar_rectangulo)
    btn_dibujar_rectangulo.pack()