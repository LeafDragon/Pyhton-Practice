# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 23:07:47 2018

@author: Frank
"""

cube = 27
epsilon = 0.01
guess = 0.0
increment = 0.01
num_guesses = 0

while abs(guess**3 - cube) >= epsilon and guess <= cube:
    guess += increment
    num_guesses += 1

print("num_guesses = ", num_guesses)

if abs(guess**3 - cube) >= epsilon:
    print("Failed on cube root of", cube)
else:
    print(guess, "is close to cube root of", cube)
