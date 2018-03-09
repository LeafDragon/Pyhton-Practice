# -*- coding: utf-8 -*-
"""
Created on Fri Mar  9 13:24:34 2018

@author: Frank
"""

cube = 27

for guess in range(cube + 1):
    if guess**3 == cube:
        print("The cube root of " + str(cube) + " is " + str(guess))
