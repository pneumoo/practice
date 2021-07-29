# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 13:27:18 2015
@author: Brian
"""

"""
Sum square difference
Problem 6
The sum of the squares of the first ten natural numbers is,
12 + 22 + ... + 102 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)2 = 552 = 3025

Hence the difference between the sum of the squares of the first 
ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first 
one hundred natural numbers and the square of the sum.
"""


#==============================================================================
# My solution
#==============================================================================

num = 100000000
a = [x for x in range(1,num+1)]


#Takes a list, n
def sumofsquares(a):
    s = 0    
    for i in range(len(a)):
        s += a[i]**2
    return(s)

#Takes a list, n
def squareofsum(a):
    return(sum(a)**2)
        

dif = squareofsum(a) - sumofsquares(a)
print(dif)            

        

#==============================================================================
# Euler Project Solution:
#==============================================================================
limit = 100000000
s = limit*(limit + 1)/2
sum_sq = (2*limit + 1)*(limit + 1)*limit/6
total = s*s - sum_sq
print(total)