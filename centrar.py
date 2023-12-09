import tkinter as tk

class FigurasApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Figuras en el Centro")
        
        # Crear un lienzo (canvas)
        self.canvas = tk.Canvas(root, width=400, height=400, bg="white")
        self.canvas.pack()

        # Dibujar un círculo en el centro
        self.dibujar_circulo()

        # Dibujar un rectángulo en el centro
        #self.dibujar_rectangulo()

        # Dibujar un rectángulo en el centro
        #self.dibujar_triangulo()

    def dibujar_circulo(self):
        x, y = self.canvas.winfo_reqwidth() / 2, self.canvas.winfo_reqheight() / 2
        radio = 50
        self.canvas.create_oval(x - radio, y - radio, x + radio, y + radio, fill="blue")

    def dibujar_rectangulo(self):
        x, y = self.canvas.winfo_reqwidth() / 2, self.canvas.winfo_reqheight() / 2
        ancho, alto = 100, 60
        self.canvas.create_rectangle(x - ancho / 2, y - alto / 2, x + ancho / 2, y + alto / 2, fill="green")

    def dibujar_triangulo(self):
        x, y = self.canvas.winfo_reqwidth() / 2, self.canvas.winfo_reqheight() / 2
        base, altura, hipotenusa = 20, 10, 18
        self.canvas.create_polygon(x - base / 2, y - altura / 2, x + base / 2, y + hipotenusa / 2, x - base / 2, y + hipotenusa / 2, fill="black")

if __name__ == "__main__":
    root = tk.Tk()
    app = FigurasApp(root)
    root.mainloop()
