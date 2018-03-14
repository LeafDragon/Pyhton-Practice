# -*- coding: utf-8 -*-
"""
created on 2018-03-13

@author Frank Dip
"""
# Using the slicing method
s = "hello boy"

s = s[:6] + "B" + s[7:]

print(s)

# Using the find method
s = "hello boy"

s = s[:s.find("b")] + "B" + s[s.find("b") + 1:]

print(s)
