# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 13:27:18 2015
@author: Brian
"""

"""
Largest palindrome product
Problem 4
A palindromic number reads the same both ways. 
The largest palindrome made from the product of two 
2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product 
of two 3-digit numbers.
"""


#==============================================================================
# My solution  
#==============================================================================

def checkpal(n):
    a=str(n)
    b=a[::-1]
    if b == a:
        return(True)
    else:
        return(False)

num1 = 999
num2 = 999

for i in range(10):
    for j in range(100):
        n = (num1 - i) * (num2 - j)
        a = checkpal(n)
        if a == True:
            print((num1-i), (num2-j), n)



#==============================================================================
# Euler Project Solution:
#==============================================================================
