import tkinter as tk
from tkinter import * 
from tkinter.ttk import *
from tkinter import messagebox
from math import pi

def calcular_area_perimetro_cuadrado(lado):
    area = lado ** 2
    perimetro = 4 * lado
    return area, perimetro

def calcular_area_perimetro_rectangulo(ancho, largo):
    area = ancho * largo
    perimetro = 2*(ancho + largo)
    return area, perimetro

def calcular_area_perimetro_triangulo(base, altura, hipotenusa):
    area = (base * altura) / 2
    perimetro = base + altura + hipotenusa
    return area, perimetro

def calcular_area_perimetro_circulo(radio):
    area = pi * radio ** 2
    perimetro = 2 * pi * radio
    return area, perimetro

def mostrar_ventana_circulo():
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
            root = tk.Tk()
            canvas = tk.Canvas(root, width=400, height=400, bg="white")
            canvas.pack()
            x, y = canvas.winfo_reqwidth() / 2, canvas.winfo_reqheight() / 2
            radio = float(entry_radio_circulo.get())

            if radio <= 0:
                messagebox.showerror("Error", "Por favor, no ingrese números negativos.")
            else:
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

def mostrar_ventana_rectangulo():
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
            root = tk.Tk()
            canvas = tk.Canvas(root, width=400, height=400, bg="white")
            canvas.pack()
            x, y = canvas.winfo_reqwidth() / 2, canvas.winfo_reqheight() / 2
            largo, ancho = float(entry_largo_rectangulo.get()), float(entry_ancho_rectangulo.get())
            
            if largo <= 0 or ancho <= 0:
                messagebox.showerror("Error", "Por favor, no ingrese números negativos.")
            else:
                canvas.create_rectangle(x - largo / 2, y - ancho / 2, x + largo / 2, y + ancho / 2, fill="white", outline='black')

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

def mostrar_ventana_cuadrado():
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
            root = tk.Tk()
            canvas = tk.Canvas(root, width=400, height=400, bg="white")
            canvas.pack()
            x, y = canvas.winfo_reqwidth() / 2, canvas.winfo_reqheight() / 2
            lado = float(entry_lado_cuadrado.get())

            if lado <= 0:
                messagebox.showerror("Error", "Por favor, no ingrese números negativos.")
            else:
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

def mostrar_ventana_triangulo():
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

# Crear la ventana principal
ventana_principal = tk.Tk()
ventana_principal.title("Calculadora de Figuras")

# Menú para seleccionar la figura
menu_figura = tk.Menu(ventana_principal)
ventana_principal.config(menu=menu_figura)

menu_figura.add_command(label="Cuadrado", command=mostrar_ventana_cuadrado)
menu_figura.add_command(label="Rectangulo", command=mostrar_ventana_rectangulo)
menu_figura.add_command(label="Triángulo Rectángulo", command=mostrar_ventana_triangulo)
menu_figura.add_command(label='Circulo', command=mostrar_ventana_circulo)

# Iniciar el bucle de eventos de la ventana principal
ventana_principal.mainloop()