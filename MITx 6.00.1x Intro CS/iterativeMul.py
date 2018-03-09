# -*- coding: utf-8 -*-
"""
Created on Fri Mar  9 12:59:27 2018

@author: Frank Dip
"""

x = 5
ans = 0
itersLeft = x

while (itersLeft != 0):
    ans += x
    itersLeft -= 1

print(str(x) + " * " + str(x) + " = " + str(ans))
