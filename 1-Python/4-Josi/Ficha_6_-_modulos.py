# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 09:26:50 2020

@author: Miguel Correia
"""

#Exercicio 1.a.

def spherePerimeter(r):
    import math
    return (2*math.pi*r)
def sphereArea(r):
    import math
    return (math.pi*(r**2))

#Exercicio 1.b.

def squarePerimeter(l):
    return (4*l)
def squareArea(l):
    return (l**2)

#Exercicio 1.c.

try:
    raio=int(input("Insira um valor para o raio e o lado de um quadrado: "))
    print("O perimetro do quadrado é",squarePerimeter(raio))
    print("A área do quadrado é",squareArea(raio))
    print("O perimetro do circulo é",spherePerimeter(raio))
    print("A área do circulo é",sphereArea(raio))
except:
    print("Insira um número válido.")


#Exercicio 1.d.

try:
    raio=int(input("Insira um valor para o raio: "))
    print("O perimetro do quadrado é",squarePerimeter((2*raio)))
    print("A área do quadrado é",squareArea((2*raio)))
    print("O perimetro do circulo é",spherePerimeter(raio))
    print("A área do circulo é",sphereArea(raio))
except:
    print("Insira um número válido.")