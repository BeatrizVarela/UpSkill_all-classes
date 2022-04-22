# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 12:44:32 2020

@author: Ana Beatriz Varela
"""

# ************************
# repository url: https://bitbucket.org/BeatrizVarela/python-code/src/master/
# ************************

'''
Ficha 2
'''

'''
1. Considere a seguinte função:
    
def imprimeDivisaoInteira(x, y):
    if y == 0:
        print "Divisao por zero”
    else:
        print x//y
        
a. O que faz esta função?
'''

def imprimeDivisaoInteira(x, y):
    if y == 0:
        print("Divisao por zero")
    else:
        print(x // y)

imprimeDivisaoInteira(8, 2) # 4
imprimeDivisaoInteira(8, 0) # Divisao por zero

# Esta função analisa se o valor de y é 0 ou não. Caso seja, será apresentada
# uma string que avise que esta é uma divisão por zero. Caso não seja 0,
# a função calcula o quociente entre x (dividendo) e y (divisor).


'''
b. Qual o resultado da seguinte sequência de comandos?
imprimeDivisaoInteira(4, 2)
imprimeDivisaoInteira(2, 4)
imprimeDivisaoInteira(3, 0)
help(imprimeDivisaoInteira)
imprimeDivisaoInteira()
'''

def imprimeDivisaoInteira(x, y):
    if y == 0:
        print("Divisao por zero")
    else:
        print(x // y)
    
imprimeDivisaoInteira(4, 2)     # chama a função, resultado = 2
imprimeDivisaoInteira(2, 4)     # chama a função, resultado = 0
imprimeDivisaoInteira(3, 0)     # Divisao por zero
help(imprimeDivisaoInteira)     # Help on function imprimeDivisaoInteira in module __main__: imprimeDivisaoInteira(x, y)
imprimeDivisaoInteira()         # TypeError: imprimeDivisaoInteira() missing 2 required positional arguments: 'x' and 'y'


'''
c. Altere a definição da função de modo a adoptar a abordagem da programação
por contratos (recorrendo a uma docstring) em vez da abordagem da programação 
defensiva.
'''

def imprimeDivisaoInteira(x, y):
    '''
    
    Parameters
    ----------
    x : int
        dividendo
    y : int
        divisor

    Returns (x // y)
    -------
    None.

    '''

    return x // y


'''
2. Considere a seguinte função:
    
def potencia(a, b):
    return a**b

a. O que faz a seguinte sequência de comandos?

a = 2
b = 3
potencia(b, a)
potencia(a, b)
print potencia(b, a)
print potencia(a, b)
print potencia(2,0)
print potencia(2)
'''

def potencia(a, b):
    return a**b

a = 2                   # valor de a
b = 3                   # valor de b
potencia(b, a)          # chama a função, 3 elevado a 2
potencia(a, b)          # chama a função, 2 elevado a 3
print(potencia(b, a))   # 9
print(potencia(a, b))   # 8
print(potencia(2,0))    # 1
print(potencia(2))      # TypeError: potencia() missing 1 required positional argument: 'b'


'''
b. Escreva uma nova função potenciaP que receba apenas um número inteiro a 
e retorne a**a.
'''

def potenciaP(a):
    return a**a

print(potenciaP(2))     # 2**2 = 4
print(potenciaP(3))     # 3**3 = 27


'''
c. Escreva uma nova versão da função potencia que possa ser chamada com 
dois ou com um argumento e, consoante o caso, execute a**b ou a**a.
'''

def potencia(a, b = None):
        return a**a if b == None else a**b
a = 2
b = 3

print(potencia(a, b))
print(potencia(a))


'''
3. Considere o seguinte programa:
    
a = 4
def printFuncao():
    a = 17
    print("Dentro da funcao: ", a)
printFuncao()
print("Fora da funcao: ", a)

a. Qual é o resultado de executar este programa?
'''

a = 4
def printFuncao():
    a = 17
    print("Dentro da funcao: ", a)
printFuncao()
print("Fora da funcao: ", a)

# Dentro da funcao:  17 ---> variável local
# Fora da funcao:  4    ---> variável global


'''
b. O que é uma variável global? E uma variável local?
'''

# a = 4 está fora da função, por isso é uma variável global
# a = 17 está dentro da função, logo é uma variável local


'''
4. Considere o seguinte código:
    
def somaDivisores(num):
    """
    Soma de divisores de um numero dado
    Requires:
     num seja int e num > 0
     Ensures: um int correspondente à soma dos divisores
     de num que sejam maiores que 1 e menores que num
     """
     
a. Como cliente da função somaDivisores, o que deve satisfazer para a função 
cumprir o contrato?
'''

def somaDivisores(num):
    """
    Soma de divisores de um numero dado
    Requires:
        num seja int e num > 0
    Ensures: um int correspondente à soma dos divisores
    de num que sejam maiores que 1 e menores que num
     """

# Deve receber um número inteiro e maior que 0


'''
b. E o que obtém da função se a chamar satisfazendo a sua pré-condição?
'''

# Um número inteiro correspondente à soma dos divisores do número inteiro
# introduzido (num), que sejam maiores que 1 e menores que num.


'''
5. Crie um programa que pergunte sucessivamente ao utilizador um número 
inteiro positivo e imprima a soma dos seus divisores. A execução do programa 
deve terminar quando o utilizador introduzir um número negativo. 
Nota: assuma que a função somaDivisores, apresentada no exercício anterior, 
se encontra definida.
'''

def SomaDivisores(num):
    divisors = [1]
    for i in range(2, num):
        if (num % i)==0:
            divisors.append(i)
    return sum(divisors)

while True:
    num = int(input("Escreva um número inteiro positivo: "))
    print(SomaDivisores(num))
    if num <= -1:
        print("O número devia ser positivo. \nAdeus.")
        break
 

'''
6. Considere o seguinte programa:
    
DIA_ATUAL = 2
MES_ATUAL = 11
ANO_ATUAL = 2015

print "Dados do Pai"
anoPai = int(raw_input("Introduza o ano de nascimento: "))
mesPai = int(raw_input("Introduza o mes de nascimento: "))
diaPai = int(raw_input("Introduza o dia de nascimento: "))

print "Dados da Mae"
anoMae = int(raw_input("Introduza o ano de nascimento: "))
mesMae = int(raw_input("Introduza o mes de nascimento: "))
diaMae = int(raw_input("Introduza o dia de nascimento: "))

if mesPai > MES_ATUAL or \
    (mesPai == MES_ATUAL and diaPai > DIA_ATUAL):
    print("Pai tem", ANO_ATUAL - anoPai - 1, "ano(s)")
else:
    print("Pai tem", ANO_ATUAL - anoPai, "ano(s)")

if mesMae > MES_ATUAL or \
    (mesMae == MES_ATUAL and diaMae > DIA_ATUAL):
    print("Mae tem", ANO_ATUAL - anoMae - 1, "ano(s)")
else:
    print("Mae tem", ANO_ATUAL - anoMae, "ano(s)")

Recorrendo a funções, simplifique o programa apresentado eliminando a 
repetição de código.
'''

import datetime

x = datetime.datetime.now()
DIA_ATUAL = x.day
MES_ATUAL = x.month
ANO_ATUAL = x.year

def dados(parente):
    if parente == "Pai":
        print("Dados do Pai")
    else:
        print("Dados da Mãe")
    ano=int(input("Introduza o ano do nascimento: "))
    mes=int(input("Introduza o mês do nascimento: "))
    dia=int(input("Introduza o dia do nascimento: "))
    return (ano, mes, dia, parente)

def anos_atuais(ano,mes,dia,parente):
    if mes > MES_ATUAL or (mes == MES_ATUAL and dia > DIA_ATUAL):
        print(parente,"tem",ANO_ATUAL-ano-1,"anos")
    else:
        print(parente,"tem",ANO_ATUAL-ano,"anos")

dadosPai=dados("Pai")
dadosMae=dados("Mãe")

anos_atuais(dadosPai[0],dadosPai[1],dadosPai[2],dadosPai[3])
anos_atuais(dadosMae[0],dadosMae[1],dadosMae[2],dadosMae[3])


'''
7. Escreva uma função que receba dois números inteiros e devolva o maior 
deles. Inclua o contrato da função. Teste a função escrevendo um programa 
que receba dois números inteiros do utilizador e imprima o resultado da 
chamada à função desenvolvida. Como teria de fazer para determinar o menor 
de dois números com uma segunda função que tirasse partido de chamar a 
primeira?
'''

def maior(x, y):
    if x > y:
        return x
    else:
        return y

def menor(x, y):
    if x < y:
        return x
    else:
        return y
    
x = int(input("Escreva um número: "))
y = int(input("Escreva outro número: "))

print("\nO número de maior valor é",maior(x,y))
print("\nO número de menor valor é",menor(x,y))


'''
8. Escreva uma função (o contrato não pode ser esquecido) que elimine a 
casa das unidades de um número inteiro. Por exemplo, retira(537) devolve 53. 
Se o argumento só tiver algarismo das unidades, a função deve devolver 0. 
Teste a função escrevendo um programa que receba um número inteiro do 
utilizador e imprima o resultado de chamada à função desenvolvida.
'''

def remove(n):
    '''

    Parameters
    ----------
    n : int
        com mais de duas casas decimais

    Returns (n // 10)
    -------
    int
        casa das unidades eliminada

    '''
    return n // 10

n = int(input("Escreva um número maior que 10: "))
print(remove(n))


# Outra solução

b = 5655

def unidades (a): 
    a = str(a)
    if len(a) < 2:
        return 0
    else:
        return int(a[:-1])

print(unidades(b))


'''
9. Escreva uma função que acrescente um 0 no final de um número inteiro. 
Por exemplo, aumenta(73) devolve 730 (se esquecer o contrato a definição 
da função está incompleta). aumenta(0) deve devolver 0. Teste a função 
escrevendo um programa que receba um número inteiro do utilizador e imprima 
o resultado da chamada à função desenvolvida.
'''

def acrescenta(n):
    '''
    
    Parameters
    ----------
    n : int
        qualquer int.

    Returns
    -------
    int
        int com 0 acrescentado ao final.

    '''
    return n * 10

n = int(input("Escreva um número: "))
print(acrescenta(n))


'''
10. Escreva uma função que receba um número inteiro e devolva a soma dos 
divisores próprios desse número

def somaDivisores(num):
     """
     Soma dos divisores próprios de um numero dado.
     Requires:
         num seja int e num > 0
     Ensures:
         um int correspondente à soma dos divisores
         de num que sejam maiores que 1 e menores que num
     """
     
Teste a função escrevendo um programa que receba um número inteiro do 
utilizador e imprima o resultado da chamada à função desenvolvida.
'''

def SomaDivisores(num):
    divisors = [1]
    for i in range(2, num):
        if (num % i)==0:
            divisors.append(i)
    return sum(divisors)

while True:
    num = int(input("Escreva um número inteiro positivo: "))
    print(SomaDivisores(num))
    if num <= -1:
        print("O número devia ser positivo. \nAdeus.")
        break

# Divisor próprio é o próprio número

'''
11. Escreva uma função que verifique se um dado número dado é primo. 
Relembre que um número é primo se é maior do que 1 e não tem divisores 
próprios. Teste a função escrevendo um programa que receba um número 
inteiro do utilizador e imprima o resultado da chamada à função desenvolvida.
'''

def primo(num):
    if num > 1:
       for i in range(2, num+1):
           if (num % i) == 0:
               print(num,"não é número primo.")
               break
       else:
           print(num,"é número primo.")
    else:
       print(num,"não é número primo.")

num = int(input("Escreva um número: "))
primo(num)


'''
12. Usando a função do exercício anterior, escreva um programa que receba 
um número inteiro n maior do que 2 e escreva no ecrã quantos números primos 
existem entre 2 e n (inclusive). Por exemplo, existem 1000 números primos 
entre 2 e 7919. Teste a função escrevendo um programa que receba um número 
inteiro do utilizador e imprima o resultado de chamada à função desenvolvida. 
Explique, nesta situação, em que difere a programação defensiva da 
programação por contratos.
'''

def primo(num):
    if num > 1:
       for i in range(2, num+1):
           if (num // i) == (num / i) and i!=num:
               break
           elif (num // i) == 1:
               return num

def quantPrimo(n):
    lista = []
    for j in range(2, n + 1):
        if primo(j)!=None:
            lista.append(primo(num))
    return len(lista)

while True:
    n = int(input("Escreva um número inteiro maior que 2: "))
    if n > 2:
        print(f"Existem {quantPrimo(n)} números primos entre 2 e {n}")
        break
        
# ************************