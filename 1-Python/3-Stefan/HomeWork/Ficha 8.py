# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 17:37:33 2020

@author: Ana Beatriz Varela
"""

# ************************
# repository url: https://bitbucket.org/BeatrizVarela/python-code/src/master/
# ************************

'''
Ficha 8
'''

'''
1. Crie uma classe que modele uma pessoa:
a. Atributos: nome, idade, peso e altura
'''

class Pessoa:
    nome = 'Caramelo'
    idade = 20
    peso = 75
    altura = 1.75

print("Nome:",str(Pessoa.nome))
print("Idade:",str(Pessoa.idade),"anos")
print("Peso:",str(Pessoa.peso),"kgs")
print("Altura:",str(Pessoa.altura),"m")

'''
b. Métodos: Envelhercer, engordar, emagrecer, crescer. Obs: Por padrão, a cada ano que 
nossa pessoa envelhece, sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.
'''

class Pessoa:
    nome = "Caramelo"
    idade = 20
    peso = 75
    altura = 1.75
    
    def Crescer(self):
        if self.idade <= 21:
            self.altura=self.altura+0.005

    def Envelhecer(self,anos):
        for i in range(anos):
            self.crescer()
            self.idade+=1
    
    def Engordar(self,kgs):
        self.peso+=kgs
    
    def Emagrecer(self,kgs):
        self.peso-=kgs


pessoa = Pessoa()
pessoa1 = Pessoa()
print(Pessoa.Engordar(Pessoa.peso, 5))
print(Pessoa.Envelhecer(10))
print(Pessoa.Emagrecer(Pessoa.peso, 2))

print('O nome deste desgraçado é '+ str(Pessoa.nome) + ', que ainda é um baby de ' + str(Pessoa.idade) + ' anos.')
print((str(Pessoa.envelhecer)))


'''
2. Desenvolva uma classe Macaco,que possua os atributos nome e bucho (estomago) e pelo 
menos os métodos comer(), verBucho() e digerir(). Faça um programa ou teste 
interativamente, criando pelo menos dois macacos, alimentando-os com pelo menos 
3 alimentos diferentes e verificando o conteúdo do estomago a cada refeição. 
Experimente fazer com que um macaco coma o outro. 

É possível criar um macaco canibal?
'''

class macaco:
    def __init__(self,nome):
        self.bucho=[]
        self.nome=nome
        
    def verBucho(self):
        print(self.bucho)
        
    def comer(self,comida):
        self.bucho.append(comida)
        self.verBucho()
        
    def digerir(self):
        self.bucho.pop(0)
        
macaco1=macaco("Super macaco")
macaco2=macaco("Macaco comestivel")
macaco1.comer(2)
macaco1.comer("olá")
macaco1.comer(2.1)
macaco2.comer(2)
macaco2.comer("olá")
macaco2.comer(2.1)
macaco1.comer(macaco2)

'''
É possivel criar um macaco canibal porque o que está a acontecer é, 
estamos a inserir um objeto dentro de uma lista,assim todo o conteudo
do objeto está agora dentro de o macaco que comeu o outro.
'''
