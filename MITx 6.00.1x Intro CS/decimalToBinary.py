# -*- coding: utf-8 -*-
"""
Created on Fri Mar 16 17:50:17 2018

@author: Frank
"""

num = 19

if num < 0:
    isNeg = True
    num = abs(num)
else:
    isNeg = False

result = ""

if num == 0:
    result = "0"

while num > 0:
    result = str(num % 2) + result
    num //= 2

if isNeg:
    result = "-" + result

print(result)
