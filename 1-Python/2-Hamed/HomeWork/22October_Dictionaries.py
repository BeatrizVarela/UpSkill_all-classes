# -*- coding: utf-8 -*-
"""
Created on Thu Oct 23 15:44:54 2020

@author: Ana Beatriz Varela
"""

#************************
# exercise 1
# ***********************


person = {'children': ['Olivia', 'Sophia'],
          'phone':{'home': '01-4455',
                   'mobile': '918-123456'},
          'age': 48,
          'name': 'Beatriz'}


print(len(person))                  # 4

print(person['phone']['home'])      # 01-4455

print(person['phone']['mobile'])    # 918-123456

print(person['children'])           # ['Olivia', 'Sophia']
print(person['children'][0])        # Olivia

print(person.pop('age'))            # 48
