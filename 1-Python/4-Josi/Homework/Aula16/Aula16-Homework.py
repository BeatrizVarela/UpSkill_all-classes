# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 16:24:06 2020

@author: Ana Beatriz Varela
"""

# ************************
# repository url: https://bitbucket.org/BeatrizVarela/python-code/src/master/
# ************************

# ************************
# Exercicios dos 3 Graficos
# ************************

'''
https://data.oecd.org/pisa/mathematics-performance-pisa.htm#indicator-chart
Usar o ficheiro csv com os dados do PISA de matemática de Portugal 
(avaliação global da educação), para obter:
    
    a) um gráfico das médias anuais de Portugal (PRT):
'''

import pandas as pd
import matplotlib.pyplot as plt
import os

file_path = (os.getcwd()+"\\1-Python\\4-Josi\\Homework\\Aula16\\DP_LIVE_04112020161547500.csv")

df = pd.read_csv(file_path)
newdf = df[(df.LOCATION == "PRT")]

FilterBoy = newdf[(newdf.SUBJECT == "BOY")]
Boy = FilterBoy['Value'].tolist()

FilterGirl = newdf[(newdf.SUBJECT == "GIRL")]
Girl = FilterGirl['Value'].tolist()

Year = FilterGirl['TIME'].tolist()

plt.xlabel("Anos")  
plt.ylabel("Valores") 

plt.plot(Year, Boy, color = "purple")
plt.plot(Year, Girl, color = "pink")

plt.title("Médias Anuais de Portugal")
plt.legend(["Meninos", "Meninas"])

plt.show()


'''
    b) um outro de 5 outros os países(livre escolha) comparados com Portugal:
'''

import pandas as pd
import matplotlib.pyplot as plt
import os

file_path = (os.getcwd()+"\\1-Python\\4-Josi\\Homework\\Aula16\\DP_LIVE_04112020161547500.csv")

df = pd.read_csv(file_path)

PRT = df[(df.LOCATION == "PRT")]
FIN = df[(df.LOCATION == "FIN")]
JPN = df[(df.LOCATION == "JPN")]
USA = df[(df.LOCATION == "USA")]
AUS = df[(df.LOCATION == "AUS")]
SWE = df[(df.LOCATION == "SWE")]

PRTGirl = PRT[(PRT.SUBJECT == "GIRL")]
GirlP = PRTGirl['Value'].tolist()

FINGirl = FIN[(FIN.SUBJECT == "GIRL")]
GirlF = FINGirl['Value'].tolist()

JPNGirl = JPN[(JPN.SUBJECT == "GIRL")]
GirlJ = JPNGirl['Value'].tolist()

USAGirl = USA[(USA.SUBJECT == "GIRL")]
GirlU = USAGirl['Value'].tolist()

AUSGirl = AUS[(AUS.SUBJECT == "GIRL")]
GirlA = AUSGirl['Value'].tolist()

SWEGirl = SWE[(SWE.SUBJECT == "GIRL")]
GirlS = SWEGirl['Value'].tolist()

Year = PRTGirl['TIME'].tolist()

plt.xlabel("Anos")  
plt.ylabel("Valores") 

plt.plot(Year, GirlP, color = "green")
plt.plot(Year, GirlF, color = "blue")
plt.plot(Year, GirlJ, color = "red")
plt.plot(Year, GirlU, color = "yellow")
plt.plot(Year, GirlA, color = "orange")
plt.plot(Year, GirlS, color = "purple")

plt.title("Médias Anuais Comparativas (Meninas)")
plt.legend(["Portugal", "Finlandia", "Japão", "América", "Australia", "Suécia"], bbox_to_anchor=(1.4, 0.4))

plt.show()


'''
    c) um gráfico de barras com os dados em relação ao desempenho de meninos e
    meninas, usando o matplotlib
'''

import pandas as pd
import matplotlib.pyplot as plt
import os

file_path = (os.getcwd()+"\\1-Python\\4-Josi\\Homework\\Aula16\\DP_LIVE_04112020161547500.csv")

df = pd.read_csv(file_path)
newdf = df[(df.LOCATION == "PRT")]

FilterBoy = newdf[(newdf.SUBJECT == "BOY")]
Boy = FilterBoy['Value'].tolist()

FilterGirl = newdf[(newdf.SUBJECT == "GIRL")]
Girl = FilterGirl['Value'].tolist()

Year = FilterGirl['TIME'].tolist()

plt.xlabel("Anos")  
plt.ylabel("Valores") 

plt.bar(Year, Boy, color = "purple")
plt.bar(Year, Girl, color = "pink")

plt.title("Médias Anuais de Portugal")
plt.legend(["Meninos", "Meninas"])

plt.show()
