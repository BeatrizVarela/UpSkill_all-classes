# -*- coding: utf-8 -*-

# Beatriz Varela
# ************************
# exercise 6 + 7
# username Ana Beatriz Varela
# repository url: https://bitbucket.org/BeatrizVarela/python-code/src/master/

    # input:
        # student_name
        # student_age
    # output:
        # <student_name and age>
    # This code shows the student's name and age
# ************************

# print(student_name, student_age)

frase = 'Lisbon is in Portugal'

#strings começam sempre no 0, ou seja, 0 = L neste caso

print(frase) #Lisbon is in Portugal
print(frase[0]) #L
print(frase[0:6]) #Lisbon
print(frase[:6]) #Lisbon
print(frase[18]) #g
print(frase[18]+frase[14]) #go

print('')

city_name = frase[0:6]
print(city_name) #Lisbon
country_name = frase[13:21]
print(country_name) #Portugal

print('')

print(frase[-5:-1]) #tuga
print(frase[-21:-15]) #Lisbon
print(frase[-8:-5]) #Por
print(frase[-14:-12]) #is
print(frase[-8:]) #Portugal
print(frase[7:]) #is in Portugal
print(frase[-21:])#Lisbon is in Portugal
print(frase[:]) #Lisbon is in Portugal

# ↑ [:] → assume sempre a string toda

# ************************