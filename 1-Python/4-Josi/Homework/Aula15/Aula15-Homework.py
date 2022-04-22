# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 17:29:25 2020

@author: Ana Beatriz Varela
"""

# repository url: https://bitbucket.org/BeatrizVarela/python-code/src/master/

# ************************
# Homework - Aula 15
# ************************

'''
Exercise 1

- In the module that we created, provide operations with circles, namely, 
calculation of the perimeter and area given the radius. Add the sphere volume 
function code in your module
'''

import GeometryCalculation

radius = float(input("Input the circle's radius: "))
print("\nThe perimeter is", ("%.2f" % GeometryCalculation.circlePerimeter(radius)))
print("The area is", ("%.2f" % GeometryCalculation.circleArea(radius)))
print("The volume is", ("%.2f" % GeometryCalculation.circleVolume(radius)))


'''
- Provide operations with squares, namely, calculation of the perimeter and area 
given the length of the side.
'''

import GeometryCalculation

side = float(input("Input the square's side: "))
print("\nThe perimeter is", ("%.2f" % GeometryCalculation.squarePerimeter(side)))
print("The area is", ("%.2f" % GeometryCalculation.squareArea(side)))


'''
- Provide the possibility to ask the user for a value and writes on the screen 
the perimeter and the area of the circle and square based in the radius and side 
measurement.
'''

import GeometryCalculation

radius = float(input("Input the circle's radius: "))
side = float(input("Input the square's side: "))

print("\nThe perimeter of the circle is", ("%.2f" % GeometryCalculation.circlePerimeter(radius)))
print("The area of the circle is", ("%.2f" % GeometryCalculation.circleArea(radius)))

print("\nThe perimeter of the square is", ("%.2f" % GeometryCalculation.squarePerimeter(side)))
print("The area of the square is", ("%.2f" % GeometryCalculation.squareArea(side)))


'''
Exercise 2

Write a function that takes as a parameter a list of integers. The function must
return a tuple with two integer values f1 and f2, where f1 is the list element with
lowest frequency (lowest number of occurrences in the list) and f2 is the element with 
the highest frequency. Tip: use a dictionary to compute the frequencies of the list 
elements.
The following function must be implemented:

def frequencies (v)

Input =  [1, 4, 5, 1, 6, 3, 2, 1, 2, 9, 1, 4, 6, 3, 9]
Output = ([f1], [f2])     f1 = [5,7]     f2=[1]

def frequencies (v)
'''

def frequencies(v):                                 # Defining the function
    import operator
    frequency = {}                                  # Empty dictionary 
    for i in v:                                     # For every element in the list
        frequency[i] = frequency.get(i, 0) + 1      # All elements in the new dictionary are sorted as key = the element in the list, and value = number of times it's repeated
    frequency = (sorted(frequency.items(), key = operator.itemgetter(1)))
    small_freq=frequency[0][1] 
    high_freq=frequency[(len(frequency)-1)][1]
    f1 = []
    f2 = []
    for nums in frequency:
        if nums[1] == high_freq:
            f2.append(nums[0])
        elif nums[1] == small_freq:
            f1.append(nums[0])
    return f1, f2                                  # And returns the dictionary with the specifications above
   
v = [1, 4, 5, 1, 6, 3, 2, 1, 2, 9, 1, 4, 6, 3, 9, 7]
print(frequencies(v))                              

    










