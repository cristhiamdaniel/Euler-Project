#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
EULER PROJECT

@author: cristhiamdaniel
"""

'''
Largest palindrome product
Problem 4

A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

'''

#We calculate the list with the products of the 3-digit numbers
listProducts = []

# This loop is very inefficient since you get repeated products because 
# of the commutativity property of multiplication. 
# Could be improved in terms of efficiency.
for i in range(100 ,1000):
    for j in range(100,1000):
        product  = i*j
        listProducts.append(product)

# we define the function "flip", 
# which allows us to exchange the position of the digits 
# of the products obtained previously.

def flip(n):
    
    rev = 0 # the reverse variable is initialized to 0
    while(n > 0):
        a = n % 10
        rev = rev * 10 + a
        n = n // 10

    return(rev)


# we create an empty list to store all the "flip" numbers
# of each number stored in "listProducts"
listFlip = []

for j in listProducts:
    
    reverse = flip(j) # We call the function "flip"
    listFlip.append(reverse)

# We create an empty list where we are going to store all the numbers
# that are palindromes. 
# For this we compare in each position the values ​​of the
# two previously created lists.
palindromes = []
for k in range(len(listProducts)):
    if listProducts[k] == listFlip[k]:
        palindromes.append(listProducts[k])

# Finally we calculate the maximum value of the list of palindromes.
print("The largest number in the list of palindromes\
      of the product of two 3-digit numbers is:",
       max(palindromes))