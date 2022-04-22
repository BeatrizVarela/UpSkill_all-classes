"""
Escreva em linguagem Python um programa que leia um número inteiro positivo
(menor ou igual a 5) e escreva no ecrã a sua representação em numeração
romana. Segue-se um exemplo da interacção com o computador (em itálico os
dados introduzidos pelo utilizador).
"""

"""Solução 1
"""

numero_inteiro = int(input("escreva um numero"))

# casos_especiais = { 
#     1: 'I', 
#     4: 'IV', 
#     5: 'V', 
#     9: 'IX', 
#     10: 'X', 
#     40: 'XL',
#     50: 'L', 
#     90: 'XC', 
#     100: 'C', 
#     400: 'XD', 
#     500: 'D', 
#     900: 'CM', 
#     1000: 'M'
# }

# valores_casos_especiais_invertidos = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

# numero_romano = ""

# for valor in valores_casos_especiais_invertidos:
#     coeficiente = numero_inteiro // valor # quantas vezes valor dos caoss especiais está contido no número
    
#     if coeficiente != 0: # se caso especial estiver contido no número
#         for y in range(coeficiente):
#             numero_romano += casos_especiais[valor] # adicionar ao caso especial ao número o numero de vezes que foi obtido em coeficiente

#     numero_inteiro = numero_inteiro % valor # remove ao numero inteiro o valor do caso especial, o número de vezes que for possível atravês da operação de resto de divisão

# print(numero_romano)

"""Solução 2
"""

tabelaInteiroRomano =  [(1000,'M'), (900,'CM'), (500,'D'), (400,'CD'), (100,'C'), (90,'XC'), (50,'L'), (40,'XL'), (10,'X'), (9,'IX'), (5,'V'), (4,'IV'), (1,'I')]

resultado = ""
for numero, letra in tabelaInteiroRomano:
    quantos = numero_inteiro // numero
    resultado += letra * quantos
    numero_inteiro -= numero * quantos

print(resultado)