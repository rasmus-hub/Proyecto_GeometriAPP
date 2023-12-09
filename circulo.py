# Ventana de la figura del circulo para mostrar sus resultados y dibujos graficamente en la UI

import tkinter as tk
from tkinter import messagebox
from calculo import calcular_area_perimetro_circulo

def mostrar_ventana_circulo(ventana_principal):
    ventana_circulo = tk.Toplevel(ventana_principal)
    ventana_circulo.title("Circulo")

    tk.Label(ventana_circulo, text="Radio del circulo:").pack()
    entry_radio_circulo = tk.Entry(ventana_circulo)
    entry_radio_circulo.pack()

    def calcular_circulo():
        try:
            radio = float(entry_radio_circulo.get())
            if radio <= 0:
                messagebox.showerror("Error", "Por favor, no ingrese números negativos.")
            else:
                area, perimetro = calcular_area_perimetro_circulo(radio)
                messagebox.showinfo(title='Resultados', message=f"Área: {round(area, 3)}\nPerímetro: {round(perimetro, 3)}")
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese números válidos.")
    
    def dibujar_circulo():
        try:
            radio = float(entry_radio_circulo.get())

            if radio <= 0:
                messagebox.showerror("Error", "Por favor, no ingrese números negativos.")
            else:
                root = tk.Tk()
                canvas = tk.Canvas(root, width=400, height=400, bg="white")
                canvas.pack()
                x, y = canvas.winfo_reqwidth() / 2, canvas.winfo_reqheight() / 2
                if radio <= 25:
                    canvas.create_oval(x - radio, y - radio, x + radio, y + radio, fill="blue", outline='black')

                    medida_radio = canvas.create_text(x + radio, y + radio, anchor='nw')
                    canvas.itemconfig(medida_radio, text=radio)
                    canvas.insert(medida_radio, 12, 'cm')
                else:
                    canvas.create_oval(x - radio, y - radio, x + radio, y + radio, fill="white", outline='black')

                    medida_radio = canvas.create_text(x - 17, y - 8, anchor='nw')
                    canvas.itemconfig(medida_radio, text=radio)
                    canvas.insert(medida_radio, 12, 'cm')
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese números válidos.")

    btn_calcular_circulo = tk.Button(ventana_circulo, text="Calcular", command=calcular_circulo)
    btn_calcular_circulo.pack()

    btn_dibujar_circulo = tk.Button(ventana_circulo, text="Dibujar Circulo", command=dibujar_circulo)
    btn_dibujar_circulo.pack()