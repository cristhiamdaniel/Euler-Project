#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
EULER PROJECT

@author: cristhiamdaniel
"""

'''
Smallest multiple
Problem 5

2520 is the smallest number that can be divided by each of the numbers
 from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all
 of the numbers from 1 to 20?


'''

# We define the function to calculate the greatest common divisor
def GCD(a, b):
    aux = 0
    while b != 0:
        aux = b
        b = a % b
        a = aux
    return a

# We define the function that calculates the least common multiple
# by calling the GCD function
def LCM(a, b):
    return (a * b) / GCD(a, b)

# To calculate the least common multiple of several numbers
# we are going to resort to the property:
# LCM(a,b,c) = LCM(c,LCM(a,b))

# Initial values
n = 0 
lcm = 1

# As long as n is less than the limiting number provided 
# by the problem (20)
while n < 20:
    lcm = LCM(n+1, lcm)  
    n += 1
print("The smallest positive number that is evenly divisible")
print("by all of the numbers from 1 to 20 is: ", lcm)
    
