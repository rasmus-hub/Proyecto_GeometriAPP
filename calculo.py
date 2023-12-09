# calculo.py

""" Este archivo lleva consigo el calculo de áreas
y perímetros de las figuras, necesitando para
calcular el argumento necesario que en este caso
es el lado, ancho, largo o altura, entre otros, para
asi luego entregar los resultados para mostrarlos
y dibujarlos """

from math import pi

# Calcula el área y el perímetro del cuadrado
def calcular_area_perimetro_cuadrado(lado):
    area = lado ** 2
    perimetro = 4 * lado
    return area, perimetro

# Calcula el área y el perímetro del rectángulo
def calcular_area_perimetro_rectangulo(ancho, largo):
    area = ancho * largo
    perimetro = 2*(ancho + largo)
    return area, perimetro

# Calcula el área y el perímetro del triángulo rectángulo
def calcular_area_perimetro_triangulo(base, altura, hipotenusa):
    area = (base * altura) / 2
    perimetro = base + altura + hipotenusa
    return area, perimetro

# Calcula el área y el perímetro (circunferencia) del círculo
def calcular_area_perimetro_circulo(radio):
    area = pi * radio ** 2
    perimetro = 2 * pi * radio
    return area, perimetro