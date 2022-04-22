# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 20:35:05 2020

@author: Ana Beatriz Varela
"""

# repository url: https://bitbucket.org/BeatrizVarela/python-code/src/master/

# ************************
# Aula 2 - slide 24
# ************************

# day = 'Saturday'
# temperature = 30
# raining = False

day = input('What day of the week is today? (ex. Monday) ')
temperature = input("What's the current temperature? (ex. 30) ")
raining = input('Is it raining? (yes/no) ')

if day == 'Saturday' and temperature > '20' and raining == 'no' :
    print('Go out and have fun!')
elif day == 'Sunday' and temperature > '20' and raining == 'no' :
    print('Go out and have fun!')
else:
    print ("It's better to finish some Python exercises!")

# ************************