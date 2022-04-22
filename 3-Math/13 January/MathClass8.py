# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 08:54:45 2021

@author: Ana Beatriz Varela
"""

'''
Probability

Basic Probability Concepts:
    Sample Spaces and Events, Simple
    Probability, and Joint Probability,
Conditional Probability
Probability Distributions
'''

'''
Exercise

Deck of 52 cards
13 ranks: 1, 2, 3.... 10, J, Q, K, A
4 suits: clubs, diamonds, spades and hearts

What is the probability of picking 5 of Clubs from this deck?
'''
import matplotlib.pyplot as plt
import numpy as np
import random

simulation_number = 10000                                   # Numero de iteracoes
club=0; spade=0; diamont=0; heart=0; percentages=[]
for i in range(0, simulation_number):                       # Simultaion repetition
    card_points =[1,12,11,10,2,3,4,5,6,7,8,9,13]            # Sample space
    card_signs =['Heart', 'CLUB', 'DIAMOND', 'SPADE']       # Sample space
    
    random_point = random.choice(card_points)               # random.choice - Sorts one element of each list
    random_sign = random.choice(card_signs)                 # random.choice - Sorts one element of each list
    random_card = random_point, random_sign                 
    # print(random_card)
    
    ## Condition
    if(random_card[0] == 5 and random_card[1] == 'CLUB'):   # Event
        club+=1;
        
X = ['CLUB']
percentages.append(np.round(club/simulation_number*100,2))  # Calculate event ocurrences

fig = plt.figure()                                          # Bar chart
ax = fig.add_axes([0,0,1,1])                                # Bar chart
ax.bar(X,percentages)                                       # Bar chart

print(sum(percentages),'%')                                 # (Percentagem muda sempre)

# *********************************
import matplotlib.pyplot as plt
import numpy as np
import random

simulation_number = 10000                                   # Numero de iteracoes
club=0; spade=0; diamont=0; heart=0; percentages=[]
for i in range(0, simulation_number):                       # Simultaion repetition
    card_points =[1,12,11,10,2,3,4,5,6,7,8,9,13]            # Sample space
    card_signs =['Heart', 'CLUB', 'DIAMOND', 'SPADE']       # Sample space
    
    random_point = random.choice(card_points)               # random.choice - Sorts one element of each list
    random_sign = random.choice(card_signs)                 # random.choice - Sorts one element of each list
    random_card = random_point, random_sign                 
    # print(random_card)
    
    ## Condition
    if ((random_card[1] == 'Hearts') or (random_card[1] == 'Diamonds') or
        (random_card[0] == 1) and (random_card[1] == 'Spades') or
        (random_card[0] == 1) and (random_card[1] == 'Clubs')):
        club+=1;

X = ['CLUB']
percentages.append(np.round(club/simulation_number*100,2))  # Calculate event ocurrences

fig = plt.figure()                                          # Bar chart
ax = fig.add_axes([0,0,1,1])                                # Bar chart
ax.bar(X,percentages)                                       # Bar chart

print(sum(percentages),'%')                                 # (Percentagem muda sempre)

# *********************************
import matplotlib.pyplot as plt
import numpy as np
import random

simulation_number = 10000                                   # Numero de iteracoes
club=0; spade=0; diamont=0; heart=0; percentage_club=[]; percentage_spade=[]; percentages=[]
for i in range(0, simulation_number):                       # Simultaion repetition
    card_points =[1,12,11,10,2,3,4,5,6,7,8,9,13]            # Sample space
    card_signs =['Heart', 'CLUB', 'DIAMOND', 'SPADE']       # Sample space
    
    random_point = random.choice(card_points)               # random.choice - Sorts one element of each list
    random_sign = random.choice(card_signs)                 # random.choice - Sorts one element of each list
    random_card = random_point, random_sign                 
    # print(random_card)
    
    ## Condition
    if(random_card[0] == 7 and random_card[1] == 'CLUB'):
        club+=1;
    if(random_card[0] == 7 and random_card[1] == 'SPADE'):
        spade+=1;

X = ['CLUB', 'SPADE']
percentages.append(np.round((club)/simulation_number*100,2))  # Calculate event ocurrences
percentages.append(np.round((spade)/simulation_number*100,2))  # Calculate event ocurrences
print(percentages)

fig = plt.figure()                                          # Bar chart
ax = fig.add_axes([0,0,1,1])                                # Bar chart
ax.bar(X,percentages)                                       # Bar chart

print(percentages[0],'% chance of clubs') 
print(percentages[1],'% chance of spades')

'''
Exercises (page 49)
'''
import matplotlib.pyplot as plt
import numpy as np
import random

simulation_number = 10000
one=0; two=0; three=0; four=0; five=0; six=0; percentages=[]
for i in range(0, simulation_number):
    dice_points =[1,2,3,4,5,6]
    random_point = random.choice(dice_points)
    
    ## Condition
    if(random_point == 1):
        one+=1;
    if(random_point == 2):
        two+=1;
    if(random_point == 3):
        three+=1;
    if(random_point == 4):
        four+=1;
    if(random_point == 5):
        five+=1;
    if(random_point == 6):
        six+=1;
        
X = ['one','two','three','four','five','six']
percentages.append(np.round(one/simulation_number*100,2))
percentages.append(np.round(two/simulation_number*100,2))
percentages.append(np.round(three/simulation_number*100,2))
percentages.append(np.round(four/simulation_number*100,2))
percentages.append(np.round(five/simulation_number*100,2))
percentages.append(np.round(six/simulation_number*100,2))
print(percentages)

fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.bar(X,percentages)

print(percentages[0],'% chances of getting one')                    
print(percentages[1],'% chances of getting two')  
print(percentages[2],'% chances of getting three')  
print(percentages[3],'% chances of getting four')  
print(percentages[4],'% chances of getting five')  
print(percentages[5],'% chances of getting six')  

'''
Exercises (page 52)
'''
import matplotlib.pyplot as plt
import numpy as np
import random

simulation_number = 10000                                  # Numero de iteracoes
club=0; spade=0; diamont=0; heart=0; percentages=[]
for i in range(0, simulation_number):                       # Simultaion repetition
    card_points =[1]            # Sample space
    card_signs =['Heart', 'CLUB', 'DIAMOND', 'SPADE']       # Sample space
    
    random_point = random.choice(card_points)               # random.choice - Sorts one element of each list
    random_sign = random.choice(card_signs)                 # random.choice - Sorts one element of each list
    random_card = random_point, random_sign                 
    # print(random_card)
    
    ## Condition
    if (random_card[0] == 1 and (random_card[1] == 'Heart') or
        (random_card[1] == 'DIAMOND')):
        club+=1;

X = ['CLUB']
percentages.append(np.round(club/simulation_number*100,2))  # Calculate event ocurrences

fig = plt.figure()                                          # Bar chart
ax = fig.add_axes([0,0,1,1])                                # Bar chart
ax.bar(X,percentages)                                       # Bar chart

print(sum(percentages),'%')                                 # (Percentagem muda sempre)

# *********************************