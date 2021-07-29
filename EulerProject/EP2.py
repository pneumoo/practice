# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 13:27:18 2015
@author: Brian
"""

"""
Even Fibonacci numbers
Problem 2
Each new term in the Fibonacci sequence is generated 
by adding the previous two terms. By starting with 1 
and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose 
values do not exceed four million, find the sum of the 
even-valued terms.
"""


#==============================================================================
# My solution     
#==============================================================================
fib = [1,1]
i=1
while fib[i] <= 4000000:
    i += 1
    fib.append(fib[i-1] + fib[i-2])

print(fib)
fib.pop(len(fib)-1)
print(fib)

sum=0
for i in range(len(fib)):
    if fib[i]%2 == 0:
        sum += fib[i]

print(sum)
    

#==============================================================================
# Euler Project Solution:
#==============================================================================
#Trick is that every third number in the fib seq.
#is an even number...

limit = 4000000
sum = 0
a = 1
b = 1
c = a+b
while c < limit:
    sum = sum + c
    a = b+c
    b = c+a
    c = a+b

print(sum)