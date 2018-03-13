# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 01:02:34 2018

@author: Frank
"""

ans = 0
neg_flag = False
x = int(input("Enter a integer: "))

if x < 0: neg_flag = True

while ans**2 < x:
    ans += 1

if ans**2 == x:
    print("Square root of " + str(x) + " is " + str(ans))
else:
    print(str(x) + " is not a perfect square")
    if neg_flag:
        print("Just checking... did you mean " + str(-x) + "?")
