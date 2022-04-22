# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 09:07:45 2020

@author: Ana Beatriz Varela
"""

# repository url: https://bitbucket.org/BeatrizVarela/python-code/src/master/

# ************************
# Aula 1
# ************************

# Escreva em linguagem Python um programa que leia uma temperaura em graus Fahranheit
# e que a converta em Celcius

# C = (F - 32)/1.8

F = 100
C = (F - 32)/1.8
print(C)

a = float(input('Qual a temperatura em Fahrenheit? '))
C = (a - 32)//1.8               # Para que o resultado seja int em vez de float
print(C)

# ************************
# Escreva um programa que peça o ano de nascimento da pessoa e que imprima a idade 
# que a pessoa vai ter ao fim do ano

a = int(input('Em que ano nasceu? '))
x = 2020 - a
print('Tem', x , 'anos.')

# ************************
# Escreva um programa que leia uma hora em horas, minutos e segundos e que traduza
# para segundos

# a = str(input('Escreva uma hora. '))
a = '20:10:30'
x = a.split(':')
s = int(x[0]) * 3600 + int(x[1]) * 60 + int(x[2])
print(s)

#  Another solution
import datetime

s = datetime.datetime.now().second
print()
# ???

# ************************
# Se x = 1, qual o valor de x no final?

x = 1

if x == 1:          # True
    x = x + 1       # x = 2
    if x == 1:      # False
        x = x + 1
    else:
        x = x - 1   # x = 1
else:
    x = x - 1       # False

print(x)            # x = 1

# ************************
# Escreva um programa em Pyhton que recebe um número inteiro e que o representa
# em numeração romana.

# a = int(input('Escreva um número. (1 - 1000) '))

a = int(input('Escreva um número. (1 - 1000): '))

rr = {1:'I', 4:'IV', 5:'V', 9:'IX', 10:'X', 40:'XL', 50:'L', 90:'XC', 100:'C', 400:'CD', 500:'D', 900:'CM', 1000:'M'}
no = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]      

rn = ''

for x in no:
    q = a // x
    
    if q != 0:
        for _ in range(q):
            rn += rr[x]
    a = a % x 

print(rn)

# ************************
# Escreva em linguagem Python um programa que leia um ano ( > 0 ) 
# e escreva o século a que pertence

ano = int(input('Escreva um ano: '))
temp = ano // 100
rest = ano % 100

print('Século', temp if rest == 0 else temp + 1)

# ************************
# Escreva um programa que recebe ano, mês e dia em separado, e um número de dias X, 
# e devolva uma nova data X dias mais tarde

# import datetime

# ano = 2010
# mes = 12
# dia = 31

# for ano, mes, dia in datetime.datetime():
#     dia += 2

# print(dia, mes, ano)

ano = int(input('ano: '))
mes = int(input('mês: '))
dia = int(input('dia: '))
dias_add = int(input('Que dia será daqui a este número de dias? '))

meses_dias = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

# dias_mes = meses_dias[mes]

# if dia + dias_add > dias_mes:
    # mes += 1
    # dias = dias_mes[mes + 1] - 

if mes == 12 :
    dias_mes = meses_dias[mes]
    if dia + dias_add > dias_mes:
        mes = 1
        dia = dias_add - (dias_mes - dia)
        ano += 1
    else:
        dia = dia + dias_add
else:
    if ano % 4 == 0 and not (ano % 400 == 0 and ano % 100 == 0):
        dias_mes == 0
        
        if mes == 2:
            dias_mes = dias_mes[mes] + 1
        else:
            dias_mes = dias_mes[mes]
            
        if dia + dias_add > dias_mes:
            mes = 1
            dia = dias_add - (dias_mes - dia)
        else:
            dia = dia + dias_add
    else:
        dias_mes = meses_dias[mes]
        if dia + dias_add > dias_mes:
            while dia > dias_mes :
                mes = 1
                dia = dias_add - (dias_mes - dia)
                ano += 1
        else:
            dia = dia + dias_add
print(f"{ano}-{mes}-{dia}")


















