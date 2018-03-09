# -*- coding: utf-8 -*-
"""
Created on Fri Mar  9 12:48:31 2018

@author: Frank Dip
"""

mysum = 0

for i in range(5, 11, 2):
    mysum += i
    if mysum == 5:
        break
    
print(mysum)
