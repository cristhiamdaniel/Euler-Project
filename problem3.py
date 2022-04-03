#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
EULER PROJECT

@author: cristhiamdaniel
"""

'''


The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

'''


# We define a function in which we are going to pass an integer as input 
# and we are going to return the maximum value as a prime factor.
def PrimeFactor(number):
    factor = 2 # first prime factor
    list = [] # empty list to store prime factors
    while factor <= number:
        if number % factor == 0: # definition of a prime factor
        
            # we index the factor in the empty list
            #and continue with the iteration
            list.append(factor)
            number /= factor
        else:
            factor += 1
    
    # Once the list with the prime factors is obtained, 
    # we proceed to calculate the largest value of all of them 
    # through a 'for' loop
    max_value = 0

    for num in list:
        if (max_value == 0 or num > max_value):
            max_value = num

    return print('the prime factors are: ', list, 
                 'whose maximum value is', max_value)