# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 12:54:57 2020

@author: Ana Beatriz Varela
"""

# ************************
# repository url: https://bitbucket.org/BeatrizVarela/python-code/src/master/
# ************************

'''
Ficha 1
'''

'''
1. Escreva em linguagem Python um programa que leia uma temperatura em graus Fahrenheit
e escreva a correspondente em graus Celsius. A fórmula utilizada para a conversão de graus
Fahrenheit em graus Celsius é:
C = (F - 32) / 1.8
'''

F = 100
C = (F - 32)/1.8
print(C)

a = float(input('Qual a temperatura em Fahrenheit? '))
C = (a - 32)//1.8               # // - Para que o resultado seja 'int' em vez de float
print(C)


'''
2. Escreva em linguagem Python um programa que leia o ano de nascimento de uma pessoa e
escreva no écran a idade que terá no final do ano actual. Segue-se um exemplo da interação
com o computador.
Indique o ano de nascimento: 1972
No final de 2015 terá 42 ano(s).
'''

a = int(input('Em que ano nasceu? '))
x = 2020 - a
print('No final de 2020, terá', x , 'anos.')


'''
3. Escreva em linguagem Python um programa que leia um intervalo de tempo em horas,
minutos e segundos, e que depois imprima o número de segundos equivalente. Por
exemplo, 1 hora, 28 minutos e 42 segundos é equivalente a 5322 segundos.
'''

a = '20:10:30'
x = a.split(':')
s = int(x[0]) * 3600 + int(x[1]) * 60 + int(x[2])
print(s)


'''
4. Desenvolva a versão inversa do problema anterior: lê um número representando uma
duração em segundos e imprime o seu equivalente em horas, minutos e segundos. Por
exemplo, 9999 segundos é equivalente a 2 horas, 46 minutos e 39 segundos
'''
t=9999
h = t//3600
m = (t-(h*3600))//60
s = t-(h*3600+m*60)
print(h,':',m,':',s)


'''
5. Considere este excerto de código em Python:
if x == 1:
    x = x + 1
    if x == 1:
        x = x + 1
    else:
        x = x - 1
else:
    x = x - 1

a. Se no início da execução a variável x tiver o valor 1, qual o valor de x no final da
execução?
'''

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


'''
b. Qual teria de ser o valor inicial de x para que no final da execução fosse -1?
'''

x = 0

if x == 1:          # False
    x = x + 1       
    if x == 1:      
        x = x + 1
    else:
        x = x - 1   
else:
    x = x - 1       # True

print(x)            # x = -1


'''
c. Independentemente do valor inicial de x, há uma parte deste programa que nunca é
executada: qual e porquê?
'''

x = 1

if x == 1:          
    x = x + 1       
    if x == 1:      # <--------- Porque esta parte é redundante, x será sempre maior que 1 e nunca vai alcançar esta etapa
        x = x + 1   # <---------
    else:
        x = x - 1   
else:
    x = x - 1       

print(x)            


'''
6. Escreva em linguagem Python um programa que leia um número inteiro positivo (menor ou
igual a 5) e escreva no ecrã a sua representação em numeração romana. Segue-se um
exemplo da interacção com o computador (em itálico os dados introduzidos pelo utilizador).
Diga um numero: 4
IV
'''

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

'''
7. Escreva em linguagem Python um programa que leia um ano (> 0) e escreva no ecrã o século
a que este ano pertence. Relembre que o ano 1999 faz parte do século XX, 2000 ainda faz
parte do século XX e que 2001 é o primeiro ano do século XXI. Desenvolva uma versão do
programa utilizando um comando alternativo e outra utilizando apenas uma expressão
numérica. Note que int(True)=1 e que int(False)=0.
'''

ano = int(input('Escreva um ano: '))
temp = ano // 100
rest = ano % 100

print('Século', temp if rest == 0 else temp + 1)


'''
8. Escreva em linguagem Python um programa que leia uma data (ano, mês e dia em separado)
e um número inteiro x, e devolva uma nova data x dias mais à frente.
'''

ano = int(input('ano: '))
mes = int(input('mês: '))
dia = int(input('dia: '))
dias_add = int(input('Que dia será daqui a este número de dias? '))

meses_dias = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

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


'''
9. Indique os erros sintáticos no seguinte programa em Python:
    
x = 1
y = 1
while x = 1 and y < 5
    y = y + 2
'''

x = 1
y = 1
while x == 1 and y < 5:     # <--------- Faltava um = no x = 1. Faltavam os : no fim da frase
    y = y + 2


'''
10. Este programa em Python tem como objectivo escrever a tabuada do número inteiro dado
pelo utilizador. Explique porque é que este programa não termina, corrija o erro e
especifique qual o valor das variáveis n e i no final da execução do programa corrigido:
    
n = int(input("Escreve um número inteiro: "))
print("Tabuada do", n, ":")
i = 1
while i <= 10:
    print(n, "x", i, "=", n * i)
    i + 1
'''

n = int(input("Escreve um número inteiro: "))
print("Tabuada do", n, ":")

i = 1

if i == 1:
    print(n, "x", i, "=", n * i)
    while i <= 9:
        i+= 1
        print(n, "x", i, "=", n * i)

# O programa não terminava, porque o loop while não saía do i = 1. 
# n = integer - input pelo utilizador
# i = integer - de 1 a 9 com recurso ao loop while


'''
11. Considere este programa em Python:

dividendo = int(input("Dividendo: "))
divisor = int(input("Divisor: "))
resto = dividendo
quociente = 0
while resto >= divisor:
        resto = resto - divisor
        quociente = quociente + 1
        print("O quociente é", quociente, "e o resto é", resto)
a. O que faz este programa?
'''

dividendo = int(input("Dividendo: "))
divisor = int(input("Divisor: "))
resto = dividendo
quociente = 0
while resto >= divisor:
        resto = resto - divisor
        quociente = quociente + 1
        print("O quociente é", quociente, "e o resto é", resto)

# Este programa apresenta os valores inerentes aos quocientes e restos de determinada divisão,
# até que ao resto 0 ou mínimo possível


'''
b. Quais são as duas operações aritméticas disponíveis em Python que implementam a
mesma funcionalidade?
'''

print(4 % 2)        # Resto
print(4 // 2)       # Quociente


'''
c. Altere o programa de forma a que, caso o dividendo seja menor que o divisor, o
utilizador seja alertado e lhe sejam pedidos novos valores.
'''

while True:
   dividendo = int(input("Dividendo: "))
   divisor = int(input("Divisor: "))
   resto = dividendo
   quociente = 0
   if dividendo < divisor:
       print('O dividendo é menos que o divisor. Por favor, tente outra vez.')
   else:
        while resto >= divisor:
            resto = resto - divisor
            quociente = quociente + 1
            print("O quociente é", quociente, "e o resto é", resto)
        break
       

'''
d. Faça uma alteração adicional de forma a garantir também que tanto o dividendo
como o divisor são positivos.
'''

while True:
   dividendo = int(input("Dividendo: "))
   divisor = int(input("Divisor: "))
   resto = dividendo
   quociente = 0
   if dividendo < divisor:
       print('O dividendo é menos que o divisor. Por favor, tente outra vez.')
   elif dividendo < 0 or divisor < 0:
       print('Nem o dividendo nem o divisor devem ser negativos. Por favor, tente outra vez.')
   else:
        while resto >= divisor:
            resto = resto - divisor
            quociente = quociente + 1
            print("O quociente é", quociente, "e o resto é", resto)
        break


'''
12. O seguinte programa em Python escreve no ecrã os factoriais de todos os números inteiros
entre 1 e n, em que n é dado pelo utilizador:
n = int(input("Escreve um número inteiro: "))
current_n = 1
while current_n <= n:
    i = current_n
    f = 1
    while i > 1:
        f = f * i
        i = i - 1
    print("Factorial de " + str(current_n) + ": " + str(f))
    current_n = current_n + 1
Altere o programa de forma a que o programa não escreva os factoriais cujo valor é superior
a 1000. (Note que há formas mais ou menos eficientes de o fazer.)
'''

while True:
    n = int(input("Escreva um número inteiro: "))
    current_n = 1
    if n > 1000:
        print('O programa não corre número inteiros maiores que 1000. Por favor, tente outra vez.')
    else:
        while current_n <= n:
            i = current_n
            f = 1
            while i > 1:
                f *= i
                i -= 1
            print("Factorial de " + str(current_n) + ": " + str(f))
            current_n += 1
        break


'''
13. Escreva um programa em Python que peça ao utilizador um número decimal e escreva no
ecrã a sua parte inteira perguntando em seguida se o utilizador quer terminar a utilização do
programa.
'''

while True:
    numero = float(input("Escreva um número decimal: "))
    if float(numero):
        print('A parte inteira do número é:', (int(numero)))
        n = input('Quer terminar a utilização do programa? (y/n) ')
        if n == 'y':
            print('Adeuzinho!')
            break

'''
14. Escreva um programa em Python que peça ao utilizador um número inteiro k e uma
palavra w e escreva no ecrã k linhas em que cada linha i tem o número da linha i
separado por um espaço da palavra w concatenada i vezes, com i no intervalo de 1 a k.
'''

k = int(input("Escreva um número inteiro: "))
w = str(input("Escreva uma palavra: " ))

for i in range(1, k + 1):
    print(i, (w + " ") * i)


'''
15. Escreva um programa em Python que peça ao utilizador um número inteiro k e 
escreva no ecrã o resultado do piatório das potências de 3 com expoente de 0 a k.
'''

k = int(input("Escreva um número inteiro: "))
m = 1

for i in range(1, k + 1):
    m = m*3**i
print(m)


'''
16. Escreva um programa em Python que peça ao utilizador um número inteiro k 
maior do que 2 e escreva no ecrã quantos números perfeitos existem entre 2 e k 
(inclusive).
Por exemplo, existem 4 números perfeitos entre 2 e 10000 
(o 6, o 28, o 496 e o 8128).
'''

def isPerfect(k):
    Sum = 0
    for i in range(1, k):
        if k%i == 0:
            Sum += i
    return Sum == k

while True:
    k = int(input("Escreva um número inteiro maior que 2: "))
    if k > 2:
        for i in range(2, k+1):
            if isPerfect(i):
                print(i)
        break
    else:
        print("O número inteiro tem de ser maior que 2.")
        continue


'''
17. Escreva um programa em Python que peça ao utilizador um número inteiro k maior 
do que 10 e escreva no ecrã quantas capícuas existem entre 10 e k. Uma capícua é 
um número que se lê de igual forma da esquerda para a direita e da direita para a 
esquerda.
Por exemplo, entre 10 e 100 existem 9 capícuas
'''

def isPalindrome(k):
    temp = k
    rev = 0
    while (k > 0):
        dig = k % 10
        rev = rev * 10 + dig
        k = k // 10
    return temp == rev

while True:
    k = int(input("Escreva um número inteiro maior que 10: "))
    j = list()
    if k > 10:
        for i in range(10, k+1):
            if isPalindrome(i):
                j.append(i)
        print(len(j))
        break
    else:
        print("O número inteiro tem de ser maior que 10.")
        continue
# ************************