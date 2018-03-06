# -*- coding: utf-8 -*-
"""
Created on 2018-03-05

@author: Frank Dip
"""

x = 2
if x % 2 == 0:
    if x % 3 == 0:
        print("x is divisible by 2 and 3")
    else:
        print("x is divisible by 2 but not 3")
elif x % 3 == 0:
    print("x is divisible by 3 but not 2")
