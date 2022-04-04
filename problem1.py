#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
EULER PROJECT

@author: cristhiamdaniel
"""

'''
Problem 1


If we list all the natural numbers below 10 that are multiples of 3 or 5, 
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

'''


# The function receives as input an integer and 
# has as output the sum of the multiples of 3 or 5 for the input number.
def sum(number):
    list = [] # empty list
    for i in range(number):
        if i % 3 == 0  or i % 5 == 0:
            list.append(i) # multiples of 3 or 5 are appended
    sum = 0 # is initialized with the variable sum with the value of 0
    
    # a loop is used to iterate through all the elements of the list and 
    # each value is added to the previous one
    for j in list:
        sum += j
        
    return sum 