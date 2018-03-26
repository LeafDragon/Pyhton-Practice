# -*- coding: utf-8 -*-
"""
Created on 2018-03-26

@author: Frank
"""
def fib(x):
    """
    @desc assumes x an int >= 0
    @param {int} x Assumes it is an integer at least 0 or greater
    @return Fibonacci of x
    """
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x - 1) + fib(x - 2)
