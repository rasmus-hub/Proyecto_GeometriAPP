# main.py
import tkinter as tk
from cuadrado import mostrar_ventana_cuadrado
from rectangulo import mostrar_ventana_rectangulo
from triangulo import mostrar_ventana_triangulo
from circulo import mostrar_ventana_circulo

def main():

# Función principal que crea la ventana del programa y los botones para cada forma.

    ventana_principal = tk.Tk()
    ventana_principal.title("Calculadora de Figuras")

    btn_circulo = tk.Button(ventana_principal, text="Cuadrado", command=lambda: mostrar_ventana_cuadrado(ventana_principal))
    btn_circulo.pack()

    btn_circulo = tk.Button(ventana_principal, text="Rectángulo", command=lambda: mostrar_ventana_rectangulo(ventana_principal))
    btn_circulo.pack()

    btn_circulo = tk.Button(ventana_principal, text="Triángulo Rectángulo", command=lambda: mostrar_ventana_triangulo(ventana_principal))
    btn_circulo.pack()

    btn_circulo = tk.Button(ventana_principal, text="Círculo", command=lambda: mostrar_ventana_circulo(ventana_principal))
    btn_circulo.pack()

    """ Cuando se hace click en uno de los botones, se llama a la función correspondiente, que en estos casos
    se hizo modularización para separar cada archivo con sus funciones propias para mostrar la ventana de esa forma """

    ventana_principal.mainloop()

# Si el archivo se ejecuta como un script, la función main() se llama.

if __name__ == "__main__":
    main()
