# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 08:47:34 2020

@author: Ana Beatriz Varela
"""

#******************

'''
Ficha 4
4. Dados referentes a observações são frequentemente guardados em ficheiros de texto. Por
exemplo, as temperaturas lidas a várias horas do dia, ao longo de vários dias, podem ser
guardadas num ficheiro de números em vírgula flutuante, onde cada linha contém os valores
das várias temperaturas medidas num dia.

5.6 7.8 11.7 12.6 9.3 7.3
6.7 8.5 11.6 11.6 9.4 7.0
5.4 7.2 10.5 11.1 10.0 8.3

Utilizando a função media, escreva uma função médias que, dado o nome de um ficheiro de
texto como o acima, imprima as temperaturas médias diárias. Deverá imprimir um valor por
linha e tantos valores quantas as linhas do ficheiro. Sugestão: utilize o método string.split(s)
para obter a lista de palavras existentes numa string. A função media deve apanhar a
exceções referentes à utilização do ficheiro. Para isso utilize um try: finally: ou um with,
para se assegurar que fecha o ficheiro. Exceções sobre a abertura do ficheiro deverão ser
tratadas pelo chamador (ver exercício seguinte).
'''

from statistics import mean

def medias(ficheiro):
    with open(ficheiro) as file_reader:
        for line in file_reader:
            line = line.strip()
            split_line = line.split()                   # lista de strings
# Forma 1
            # for i in range(len(split_line)):
            #     split_line[i] = float(split_line[i])
# Forma 2
            # print(split_line)                         # lista de strings    
            float_list = list(map(float, split_line))
            print(round(mean(float_list),2))            # lista de floats

medias('temperaturas.txt')


# Another solution
# from statistics import mean

def medias(ficheiro):
    try:
        with open(ficheiro) as file_reader:
            for line in file_reader:
                line = line.strip()
                split_line = line.split()                   # lista de strings
    # Forma 1
                # for i in range(len(split_line)):
                #     split_line[i] = float(split_line[i])
    # Forma 2
                # print(split_line)                         # lista de strings    
                float_list = list(map(float, split_line))
                print(round(mean(float_list),2))            # lista de floats
    except:
        print('Something went worng while reading this file.')

medias('temperaturas.txt')


# COM ERROR - EXCEPT
# from statistics import mean

def medias(ficheiro):
    try:
        with open(ficheiro) as file_reader:
            for line in file_reader:
                line = line.strip()
                split_line = line.split()                   # lista de strings
    # Forma 1
                # for i in range(len(split_line)):
                #     split_line[i] = float(split_line[i])
    # Forma 2
                # print(split_line)                         # lista de strings    
                float_list = list(map(float, split_line))
                print(round(mean(float_list),2))            # lista de floats
    except:
        print('Something went worng while reading this file.')

medias('temperatura.txt')


# COM ERROR - EXCEPT
# from statistics import mean

def medias(ficheiro):
    try:
        file_reader = open(ficheiro)
        try:
            for line in file_reader:
                line = line.strip()
                split_line = line.split()                   # lista de strings
    # Forma 1
                # for i in range(len(split_line)):
                #     split_line[i] = float(split_line[i])
    # Forma 2
                # print(split_line)                         # lista de strings    
                float_list = list(map(float, split_line))
                print(round(mean(float_list),2))            # lista de floats
        except:
            print('Something went worng while reading this file.')
        finally:
            file_reader.close()
    except:
        print('What the heck is this document? Come back with another one.')

def ficheiro_falha():
    user_input = input("What's the name of the file? ")
    try:
        medias(user_input)
    except:
        print('It wasnt possible to open this file.')

medias('temperatura.txt')


#******************

with open('temperaturas.txt', newline = '') as file_reader:
    print(file_reader.read())
    print(help(open))

#******************

'''
Ficha 4
MANIPULAÇÃO DE CSV
1. Comma Separated Values (CSV) é o formato mais comum de importação/exportação de
dados para folhas de cálculo e para bases de dados. A linguagem Python conta com um
módulo para o efeito, CSV File Reading and Writing. O padrão mais comum de utilização do
CSV para leitura é o seguinte:
    
import csv

with open('ficheiro.csv', 'rU') as ficheiro_csv:
leitor = csv.reader(ficheiro_csv, delimiter=';')

No código acima leitor é um iterador. Pode ser usado num ciclo for, como por exemplo:
    
for linha in leitor:
    <fazer algo com linha>

Alternativamente, podemos chamar o método leitor.next() para obter os sucessivos
elementos no iterador. A exceção StopIteration é levandada quando tentamos fazer um
next() e não há mais elementos no iterador. A razão para usar 'rU' está relacionado com a
função open(), e não propriamente com CSV. O parâmetro 'U' (de Universal), aceita linhas
com a convenção Unix ('\n') e Windows ('\r\n'). O delimitador ';' é importante pois o formato
CVS para a língua portuguesa utiliza o ponto-e-vírgula como separador, uma vez que a
vírgula é utilizada como separador da parte decimal dos números.
'''

import csv

with open('eggs.csv', newline='') as csvfile:               # eggs.csv não tem vírgulas no texto
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar = '|')
    for row in spamreader:
        print(', '.join(row))                               # output tem vírgulas

#******************

import csv

with open('eggs.csv', newline='') as csvfile:               # eggs.csv não tem vírgulas no texto
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar = '|')
    print(spamreader.__next__())


'''
Escreva uma funçãocsvLinhaParaGrafico que leia dum ficheiro CSV o gráfico de uma função 
e o devolva. A função recebe o nome de um ficheiro. Assuma que o ficheiro é composto por 
duas linhas, a primeira contendo os valores das abcissas, a segunda os valores das ordenadas. 
Não se esqueça de converter as strings lidas do ficheiro em números em vírgula flutuante.
'''

# Um gráfico é uma lsita de tuples
# 1,2; 2,3; 3,4
# 1,5; 18,5; 19,4

# [(1.2, 1.5), (2.3, 18.5) (3.4, 19.4)]

def le_graficos (ficheiro_csv):
    grafico = []
    with open(ficheiro_csv) as csvfile:
        csv_reader = csv.reader(csvfile, delimiter = ';')
        linha1 = csv_reader.__next__()
        linha2 = csv_reader.__next__()
        for i in range(len(linha1)):
            item_linha1_com_ponto = linha1[i].replace(',','.')               # 1,2 -> 1.2
            item_linha2_com_ponto = linha2[i].replace(',','.')               # 1,2 -> 1.2
            grafico.append((float(item_linha1_com_ponto), float(item_linha2_com_ponto)))
    return grafico

print(le_graficos('graficos.csv'))

#******************

import csv

def converte(item1, item2):
    return float(item1.replace(',','.')), float(item2.replace(',','.'))      # 1,2 -> 1.2

def le_graficos (ficheiro_csv):
    grafico = []
    with open(ficheiro_csv) as csvfile:
        csv_reader = csv.reader(csvfile, delimiter = ';')
        linha1 = csv_reader.__next__()
        linha2 = csv_reader.__next__()
        grafico = list(map(converte, linha1, linha2))
        return grafico

print(le_graficos('graficos.csv'))



'''
### CLASSES E OBJECTOS ###
'''

class Myclass:
    area = 120              # variaveis da classe
    window_size = (2,3)
    
    def func(self):         # funções da classe - self referencia o objecto
        pass                # palavra reservada que indica que há código em falta. Assim o Python ignora a linha

print(Myclass.area)     


'''
Classe só tem pripriedades.
Pode ter variaveis e funções.

Para aceder aos valores de uma determinada propriedade, usa-se notação ponto, i.e., .nome da propriedade
ex: Myclass.area

Funções só podem ser acedidas por objectos da classe a menos que se consiga passar um objecto

Variaveis e funções de uma classe são chamados atributos
Tudo o que está dentro de uma classe são atributos

Metodos são funções da classe
'''


'''
INICIALIZADORES
'''
str()                       # Cria um objecto da classe str
int()                       # Cria um objecto da classe int
float()                     # Cria um objecto da classe float

Myclass()                   # É criado um objecto a partir da Classe

#******************

# *** Classe ***
class House:
    area = 120
    window_size = (2,3)
    
    def abre_porta(self):   
        pass
    
print(House.area) 
print(House.abre_porta()) 

# *** Objecto ***
House()

#******************

print(House.area) 
concrete_house = House()
concrete_house.area = 450
print(concrete_house.area) 


'''
__init__

Class creates object -> chama __init__ -> __init__ ersonaliza o layout do objecto ou personaliza os atributos do objecto

Home() -> __init__ personaliza este objecto
'''

class House:
    area = 120
    window_size = (2,3)
    
    def abre_porta(self):   
        pass
    
    def __init__(self, cor_das_paredes, cor_do_telhado):
        self.cor_das_paredes = cor_das_paredes
        self.cor_do_telhado = cor_do_telhado

concrete_house = House(0xffffff, 0x0000ff)     # 0x indica que número é hexadecimal

print(concrete_house.cor_das_paredes) 
print(concrete_house.cor_do_telhado) 

#******************

class House:
    area = 120
    window_size = (2,3)
    
    def abre_porta(self):   
        pass
    
    def __init__(self, cor_das_paredes = 0x000000, cor_do_telhado = 0x0000ff):
        self.cor_das_paredes = cor_das_paredes
        self.cor_do_telhado = cor_do_telhado

House['portas'] = 2
print(House.keys())

another_house = House()
another_house.cor_do_telhado
another_house.cor_das_paredes
another_house.portas = 2
print('Quantas portas? '+ str(another_house.portas))

del(another_house.portas)
del(another_house.area)

print('Qual a area da casa? '+ str(another_house.area))         # vai dar erro, porque apagou-se a area - del()

and_another_house = House()
print(and_another_house.area)                                   # Também vai dar erro. Cuidado ao usar o delete

#******************

# Tipo um dicionário!
house = {'area': 120, 'window_size': (2,3)}

#******************

a = range(1,2)
a.start         # 1
a.stop          # 2

#******************

'''
HERANÇA

Usar os atributos definidos nas outras classes

'''

class Pais:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

class Eu(Pais):
    pass

eu = Eu('Stefan Postolache', 24)
print('O meu nome é '+ str(eu.nome))
print('A minha idade é ' + str(eu.idade))

'''
SUPER().__INIT__(x,y)

É usado para definir a idade e o nome da classe Pais para a classe Eu

'''

class Pais:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

class Eu(Pais):
    def __init__(self, nome, idade, hobby):
        super().__init__(nome, idade)
        self.hobby = hobby

eu = Eu('Stefan Postolache', 24, 'jogar à bola')
print('O meu nome é '+ str(eu.nome))
print('A minha idade é ' + str(eu.idade))
print('O meu hobby é ' + str(eu.hobby))

#******************


'''
Ficha 8
1. Crie uma classe que modele uma pessoa:
a. Atributos: nome, idade, peso e altura
'''

# class Pessoa:
#     nome = 'Caramelo'
#     idade = 20
#     peso = 80
#     altura = 1.75


'''
b. Métodos: Envelhercer, engordar, emagrecer, crescer.
Obs: Por padrão, a cada ano que nossa pessoa envelhece, sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.
'''

class Pessoa:
    nome = 'Caramelo'
    idade = 19
    peso = 70
    altura = 1.75
    def __init__(self, idade, peso, altura, envelhecer, engordar, emagercer, crescer):
        self.idade + 1 = envelhecer
        self.engordar = peso + 1
        self.emagercer = peso - 1
        self.crescer = altura + 0.5

print('O nome deste desgraçado é '+ str(Pessoa.nome) + ', que ainda é um baby de ' + str(Pessoa.idade) + ' anos.')
print((str(Pessoa.envelhecer)))



'''
2. Desenvolva uma classe Macaco,que possua os atributos nome e bucho (estomago) e pelo menos os métodos 
comer(), verBucho() e digerir(). Faça um programa ou teste interativamente, criando pelo menos dois macacos, 
alimentando-os com pelo menos 3 alimentos diferentes e verificando o conteúdo do estomago a cada refeição. 
Experimente fazer com que um macaco coma o outro. É possível criar um macaco canibal?
'''