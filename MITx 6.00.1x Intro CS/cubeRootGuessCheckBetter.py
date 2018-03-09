# -*- coding: utf-8 -*-
"""
Created on Fri Mar  9 13:47:04 2018

@author: Frank
"""

cube = -27

for guess in range(abs(cube) + 1):
    if guess**3 >= abs(cube):
        break

if guess**3 != abs(cube):
    print(str(cube) + " is not a perfect cube")
else:
    if cube < 0:
        guess = -guess
    print("The cube root of " + str(cube) + " is " + str(guess))
