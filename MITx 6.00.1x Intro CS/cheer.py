# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 15:39:56 2018

@author: Frank
"""

an_letter = "aefhilmnorsxAEFHILMNORSX"

word = input("Input a word to be cheered: ")
times = int(input("Enthusiasm level (1-10):"))
i = 0

while i < len(word):
    char = word[i]
    if char in an_letter:
        print("Give me an " + char + "! " + char)
    else:
        print("Give me a " + char + "! " + char)
    i += 1
print("What does that spell?")
for i in range(times):
    print(word + " !!!")
