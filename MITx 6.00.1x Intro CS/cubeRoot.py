# -*- coding: utf-8 -*-
"""
Created on Fri Mar  9 13:13:06 2018

@author: Frank
"""

x = int(input("Enter a perfect cube: "))

ans = 0
while ans**3 < x:
    ans += 1

print("The cubed root of " + str(x) + " is " + str(ans))
