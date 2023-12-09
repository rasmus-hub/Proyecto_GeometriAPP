# Ventana de la figura del triangulo rectangulo para mostrar sus resultados y dibujos graficamente en la UI

import tkinter as tk
from tkinter import messagebox
from calculo import calcular_area_perimetro_triangulo

def mostrar_ventana_triangulo(ventana_principal):
    ventana_triangulo = tk.Toplevel(ventana_principal)
    ventana_triangulo.title("Triángulo Rectángulo")

    tk.Label(ventana_triangulo, text="Base del triángulo:").pack()
    entry_base_triangulo = tk.Entry(ventana_triangulo)
    entry_base_triangulo.pack()

    tk.Label(ventana_triangulo, text="Altura del triángulo:").pack()
    entry_altura_triangulo = tk.Entry(ventana_triangulo)
    entry_altura_triangulo.pack()

    tk.Label(ventana_triangulo, text="Hipotenusa del triángulo:").pack()
    entry_hipotenusa_triangulo = tk.Entry(ventana_triangulo)
    entry_hipotenusa_triangulo.pack()

    def calcular_triangulo():
        try:
            base = float(entry_base_triangulo.get())
            altura = float(entry_altura_triangulo.get())
            hipotenusa = float(entry_hipotenusa_triangulo.get())
            if base <= 0 or altura <= 0 or hipotenusa <= 0:
                messagebox.showerror("Error", "Por favor, no ingrese números negativos.")
            else:
                area, perimetro = calcular_area_perimetro_triangulo(base, altura, hipotenusa)
                messagebox.showinfo(title='Resultados', message=f'Área: {round(area, 3)}\nPerímetro: {round(perimetro, 3)}')
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese números válidos.")
    
    def dibujar_triangulo():
        try:
            base = float(entry_base_triangulo.get())
            altura = float(entry_altura_triangulo.get())
            hipotenusa = float(entry_hipotenusa_triangulo.get())

            if base <= 0 or altura <= 0 or hipotenusa <= 0:
                messagebox.showerror("Error", "Por favor, no ingrese números negativos.")
            else:
                root = tk.Tk()
                canvas = tk.Canvas(root, width=400, height=400, bg="white")
                canvas.pack()
                x, y = canvas.winfo_reqwidth() / 2, canvas.winfo_reqheight() / 2
                canvas.create_polygon(x - base / 2, y - altura / 2, x + base / 2, y + hipotenusa / 2, x - base / 2, y + hipotenusa / 2, fill="blue", outline='black')

                medida_base = canvas.create_text(x - base / 2, (y + hipotenusa / 2) + 5, anchor='nw')
                canvas.itemconfig(medida_base, text=base)
                canvas.insert(medida_base, 12, 'cm')

                medida_altura = canvas.create_text((x - base / 2) - 20, y + hipotenusa / 2, anchor='nw', angle=90)
                canvas.itemconfig(medida_altura, text=altura)
                canvas.insert(medida_altura, 12, 'cm')

                medida_hipotenusa = canvas.create_text((x - base / 2) + 35, (y - altura / 2), anchor='nw')
                canvas.itemconfig(medida_hipotenusa, text=hipotenusa)
                canvas.insert(medida_hipotenusa, 12, 'cm')
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese números válidos.")

    btn_calcular_triangulo = tk.Button(ventana_triangulo, text="Calcular", command=calcular_triangulo)
    btn_calcular_triangulo.pack()

    btn_dibujar_triangulo = tk.Button(ventana_triangulo, text='Dibujar Triangulo', command=dibujar_triangulo)
    btn_dibujar_triangulo.pack()