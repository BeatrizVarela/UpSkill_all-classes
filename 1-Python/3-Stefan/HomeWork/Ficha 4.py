# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 11:00:50 2020

@author: Ana Beatriz Varela
"""

# ************************
# repository url: https://bitbucket.org/BeatrizVarela/python-code/src/master/
# ************************

'''
Ficha 4
'''

'''
1. Suponha que executava os seguintes programas. Qual seria o resultado?
1.
out_file = open(“outFile.txt”, 'w')
for i in range(100):
    out_file.write(str(i))
'''

out_file = open("outFile.txt", 'w')
for i in range(100):
    out_file.write(str(i))


# O ficheiro .txt é criado e a sua informação é substituída pelos números de 1 a 99.


'''
2.
in_file = open(“inFile.txt”,'r')
indata = in_file.read()
in_file.close()
indata = in_file.read()
in_file.close()
'''

in_file = open("outFile.txt",'r')
indata = in_file.read()
in_file.close()
indata = in_file.read()
in_file.close()


# O ficheiro .txt é aberto, lido na sua totalidade e, finalmente, fechado.
# No entanto, ao chamar novamente a variável indata após o fecho do ficheiro, recebe-se o erro "ValueError: I/O operation on closed file." 


'''
3.
in_file = open(“inFile.txt”,'r')
print(in_file.readline())
in_file = open(“inFile.txt” ,'r'))
print(in_file.readline())
in_file.close()
'''

in_file = open("outFile.txt",'r')
print(in_file.readline())
in_file = open("outFile.txt",'r')
print(in_file.readline())
in_file.close()


# O ficheiro .txt é aberto e é impressa 2 vezes a primeira linha do ficheiro.


'''
2. Escreva um programa que leia um ficheiro de texto linha a linha e escreva o seu 
conteúdo no ecrã.
'''

with open("C:\\Users\\User\\python-code\\3-Stefan\\HomeWork\\LoremIpsum.txt", "r") as file:
    for line in file:
        print(line)


'''
3. Modifique o programa da alínea anterior de forma a aparecer também o número de cada
linha.
'''

with open("C:\\Users\\User\\python-code\\3-Stefan\\HomeWork\\LoremIpsum.txt", "r") as file:
    for num, line in enumerate(file, 1):
        print(num, line)


'''
4. Dados referentes a observações são frequentemente guardados em ficheiros de texto.
Por exemplo, as temperaturas lidas a várias horas do dia, ao longo de vários dias, 
podem ser guardadas num ficheiro de números em vírgula flutuante, onde cada linha 
contém os valores das várias temperaturas medidas num dia.

5.6 7.8 11.7 12.6 9.3 7.3
6.7 8.5 11.6 11.6 9.4 7.0
5.4 7.2 10.5 11.1 10.0 8.3

Utilizando a função media, escreva uma função médias que, dado o nome de um ficheiro
de texto como o acima, imprima as temperaturas médias diárias. Deverá imprimir um
valor por linha e tantos valores quantas as linhas do ficheiro.
Sugestão: utilize o método string.split(s) para obter a lista de palavras existentes 
numa string. 

A função media deve apanhar a exceções referentes à utilização do ficheiro.
Para isso utilize um try: finally: ou um with, para se assegurar que fecha o ficheiro.
Exceções sobre a abertura do ficheiro deverão ser tratadas pelo chamador
(ver exercício seguinte).
'''

from statistics import mean

def medias(ficheiro):
    try:
        with open(ficheiro) as file_reader:
            for line in file_reader:
                line = line.strip()
                split_line = line.split()
                float_list = list(map(float, split_line))
                print(round(mean(float_list),2))
    except:
        print('Something went worng while reading this file.')

medias('temperaturas.txt')


'''
5. Escreva uma função principal sem parâmetros que pede ao utilizador o nome dum
ficheiro de temperaturas, e chama a função medias passando o nome do ficheiro.
Caso ocorra algum problema de acesso ao ficheiro, a função principal deve escrever 
Erro de I/O ao ler o ficheiro
'''

from statistics import mean
from pathlib import Path

def tempMean(file):
    for line in file:
        line = line.strip()
        lineSplit = line.split()
        floatList = list(map(float, lineSplit))
        print(round(mean(floatList), 2))

def IOErro():
    dataFolder = Path(str("C:\\Users\\User\\python-code\\3-Stefan\\HomeWork"))
    file = dataFolder/str(input("Insert the file name you would like to use with its extension: "))
    try:
        tempMean(open(file))
    except:
        print("ValueError: I/O operation on closed file.")


'''
6. Informação referente a símbolos químicos pode ser guardada em ficheiros de 
texto. Neste caso estamos interessados apenas no nome, número atómico e densidade 
(em g/dm3 ). Eis um exemplo:
    
Hélio 2 0.1786
Néon 10 0.9002
Argon 18 1.7818
Cripton 36 3.708
Xenon 54 5.851
Radônio 86 9.97

Hélio 2 0.1786 Néon 10 0.9002 Argon 18 1.7818 Cripton 36 3.708 Xenon 54 5.851 Radônio
86 9.97 
2Escreva uma função linha_para_elemento que dada uma linha de um ficheiro de elementos 
(uma string), produz um dicionário com chaves 'nome', 'atomico' e 'densidade'. O nome 
é do tipo string, o número atómico do tipo int e a densidade do tipo float.
'''

def linha_para_elemento(elements):
    data=elements.split(" ")
    dic_data={"name":data[0],"atomic":int(data[1]),"density":float(data[2])}
    return dic_data

with open("C:\\Users\\User\\python-code\\3-Stefan\\HomeWork\\SimbolosQuimicos.txt","r",encoding="utf-8") as file:
    # For first line only
    readLine = linha_para_elemento(file.readline())
    print(readLine)
    # For all lines
    allElements=[]
    for elements in file:
        allElements.append(linha_para_elemento(elements))
    print(allElements)


'''
7. Utilizando a função elemento_para_string, escreva uma função escrever_elementos que,
dada uma lista de dicionários representando elementos químicos e o nome de um ficheiro,
escreve o conteúdo da lista no ficheiro.
'''

def escrever_elementos(fileName, allElements):
    with open("C:\\Users\\User\\python-code\\teste.txt", "w") as file:
        for element in allElements:
            file.write(element["name"]+" ")
            file.write(str(element["atomic"])+" ")
            file.write(str(element["density"])+"\n")

fileName = input("Insira um nome para o ficheiro: ")
fileName = fileName + ".txt"
escrever_elementos(fileName, allElements)


'''
8. O arranjo de átomos em moléculas pode ser descrito em formato textual, e portanto
guardado em ficheiros. Cada molécula é descrita por um número variável de linhas: a
primeira contém o nome da molécula, as subsequentes contêm informação sobre o átomo.
A última linha, END, fecha a molécula. Cada átomo é composto pelo seu identificador,
símbolo químico, e as coordenadas tri-dimensionais. Eis o exemplo de um ficheiro contendo
duas moléculas.

COMPND AMMONIA ATOM
ATOM 1 N 0.257 -0.363 0.000
ATOM 2 H 0.257 0.727 0.000
ATOM 3 H 0.771 -0.727 0.890
ATOM 4 H 0.771 -0.727 -0.890
END

COMPND METHANOL
ATOM 1 C -0.748 -0.015 0.024
ATOM 2 O 0.558 0.420 -0.278
ATOM 3 H -1.293 -0.202 -0.901
ATOM 4 H -1.263 0.754 0.600
ATOM 5 H -0.699 -0.934 0.609
ATOM 6 H 0.716 1.404 0.137
END

Escreva uma função linha_para_atomo que, dada uma string contendo uma linha ATOM,
devolve um dicionário com chaves 'símbolo', 'id', 'x', 'y', e 'z'.
'''

def linha_para_atomo(line):
    line = line.split()
    if "ATOM" in line[0]:
            dict1 = {"símbolo":line[2],"id":line[1],"x":line[3],"y":line[4],"z":line[5]}
            return dict1
    else:
        pass
            
lista=[]
with open("C:\\Users\\User\\python-code\\3-Stefan\\HomeWork\\atomos.txt", 'r') as atoms:
                for line in atoms:
                    if linha_para_atomo(line)!=None:
                        lista.append(linha_para_atomo(line))
                    else:
                        continue

print(lista)


'''
MANIPULAÇÃO DE CSV
'''

'''
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
com a convenção Unix ('\n') e Windows ('\r\n'). O delimitador ';' é importante pois o 
formato CVS para a língua portuguesa utiliza o ponto-e-vírgula como separador, uma vez 
que a vírgula é utilizada como separador da parte decimal dos números.
'''

import csv

with open('eggs.csv', newline='') as csvfile:               # eggs.csv não tem vírgulas no texto
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar = '|')
    for row in spamreader:
        print(', '.join(row))                               # output tem vírgulas


# Outra solução

import csv

with open('eggs.csv', newline='') as csvfile:               # eggs.csv não tem vírgulas no texto
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar = '|')
    print(spamreader.__next__())


'''
Escreva uma função csvLinhaParaGrafico que leia dum ficheiro CSV o gráfico de uma função 
e o devolva. A função recebe o nome de um ficheiro. Assuma que o ficheiro é composto por 
duas linhas, a primeira contendo os valores das abcissas, a segunda os valores das 
ordenadas. Não se esqueça de converter as strings lidas do ficheiro em números em 
vírgula flutuante.
'''

import csv

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


# Outra solução

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
2. O padrão típico para escrever num ficheiro CSV é o seguinte.

import csv

with open('ficheiro.csv', 'wb') as ficheiro_csv:
    escritor = csv.writer(ficheiro_csv, delimiter=';')
    escritor.writerow([0, 1, 2, 3, 4, 5])
    escritor.writerow([0, 2, 4, 6, 8, 10])

Escreva uma função graficoParaCsvLinha que receba o nome de um ficheiro e um gráfico
(um par de listas), e escreva o gráfico no ficheiro do seguinte modo: a primeira linha 
contém as abcissas, a segunda as ordenadas
'''

def graficoParaCsvLinha(fileName,graph):
    with open(fileName, "w", newline="") as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(graph[0])
        writer.writerow(graph[1])

fileName = input("Indique um nome para o ficheiro: ")
fileName = fileName + ".csv"

graph = [[1,3,5,7], [2,4,6,8]]
graficoParaCsvLinha(fileName, graph)


'''
3. Escreva uma função graficosParaCsv que, dado o nome de um ficheiro e uma lista de
gráficos (uma lista de listas de números), escreva os gráficos num ficheiro CSV. 
Organize a informação no ficheiro do seguinte modo: a primeira coluna contém as 
abcissas, a segunda coluna contém as ordenadas da primeira função, a terceira coluna 
contém as ordenadas da segunda função, e por aí em diante. Assuma que todas as 
funções têm listas de abcissas iguais
'''

import csv

def graficoParaCsv(fileName,graph):
    with open(fileName,"w",newline = "") as file:
        x = False
        writer = csv.writer(file)
        for graphs in graphsList:
            if x==False:
                writer.writerow(graphs[0])
                x=True
            else:
                pass
            writer.writerow(graphs[1])

graphsList = [["1","2"],["3","4"],["1","2"],["5","6"],["1","2"],["7","8"]]

fileName = input("Insira um nome para o ficheiro: ")
fileName = fileName+".csv"

graficoParaCsv(fileName, graphsList)

# ************************