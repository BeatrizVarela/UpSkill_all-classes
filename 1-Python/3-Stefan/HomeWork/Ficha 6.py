# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 15:56:35 2020

@author: Ana Beatriz Varela
"""

# ************************
# repository url: https://bitbucket.org/BeatrizVarela/python-code/src/master/
# ************************

'''
Ficha 6
'''

'''
1. Construa o seguinte:
a. Um módulo que disponibiliza operações com círculos, nomeadamente, cálculo do perímetro 
e da área dado o comprimento do raio.
'''

def spherePerimeter(p):
    import math
    return round((2*math.pi*p), 2)

def sphereArea(a):
    import math
    return round((math.pi*(a**2)), 2)


'''
b. Um módulo que disponibiliza operações com quadrados, nomeadamente, cálculo do perímetro 
e da área dado o comprimento do lado.
'''

def squarePerimeter(p):
    return round((4*p), 2)

def squareArea(a):
    return round((a**2), 2)


'''
c. Um programa que recorrendo aos módulos desenvolvidos nas alíneas anteriores, peça ao 
utilizador um valor e escreva no ecrã o perímetro e a área do círculo e do quadrado em que 
o valor dado corresponde à medida do raio e do lado.
'''
  
try:
    value = int(input("Input the circle's radius/square's side: "))
    print("\nThe square's perimeter is",squarePerimeter(value))
    print("The square's area is",squareArea(value))
    print("\nThe circle's perimeter is",spherePerimeter(value))
    print("The circle's area is",sphereArea(value))
except:
    print("The input must be a valid number, please.")
    

'''
d. Um programa que recorrendo aos módulos desenvolvidos nas alíneas anteriores, peça ao 
utilizador um valor e escreva no ecrã o perímetro e a área do maior quadrado contido no 
círculo com o raio igual ao valor dado. Lembrem-se que um módulo é um conjunto de 
definições e declarações (if/else, invocações de funções)
'''

import math

squareSide = math.sqrt(value**2+value**2)
 
try:
    value = int(input("Input the circle's radius: "))
    print("\nThe perimeter of the square inscribed in a circle is",squarePerimeter(squareSide))
    print("The area of the square inscribed in a circle is",squareArea(squareSide))
    print("\nThe circle's perimeter is",spherePerimeter(value))
    print("The circle's area is",sphereArea(value))
except:
    print("The input must be a valid number, please.")

# ************************