# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 13:27:18 2015
@author: Brian
"""

"""
10001st prime
Problem 7

By listing the first six prime numbers: 2, 3, 5, 7, 
11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""


#==============================================================================
# My solution (SUCKS)
#==============================================================================
'''
#borrowed this from obscurerichard on EP
def soe(num):
    integers=[x for x in range(2, num)]
    p=2
    while p < num:
        for n in [i for i in range((p - 1)*2, len(integers), p)]:
            integers[n] = None
        p+=1
    return(filter(lambda x:  x != None, integers))

a = soe(150000)

primes = []
for i in a:
    primes.append(i)
    
print(max(primes),len(primes))

print(primes[10000])
'''
#==============================================================================
# Euler Project Solution: (AWESOME!)
#==============================================================================

def isPrime(n):
    if n == 1:          #1 is not a prime number
        return(False)
    elif n < 4:         #2, 3 are prime
        return(True)
    elif n%2 == 0:      #if divisible by 2, its not prime
        return(False)
    elif n < 9:         #have already excluded 4,6,8
        return(True)
    elif n%3 == 0:      #if divisible by 3, its not prime
        return(False)
    else:
        r = int(n**0.5)         #root of n (largest possible)
        f = 5
        # all primes 3< can be written as (6k +/- 1)                  
        while f <= r:
            if n%f == 0:
                return(False)
                break
            elif n%(f+2) == 0:
                return(False)
                break
            else:
                f += 6
        return(True)
        
# This loop finds the first x-number of primes, defined
# by "limit". It can handle up to about the first 500,000
# primes before it starts really slowing down.        
limit = 10002
primes = []
p = 0 #counter for len(primes)
l = 1 #increments the number that's being checked
while p != limit:
    if isPrime(l+1) == True:
        primes.append(l+1)
        p += 1
        l += 1
    else:
        l += 1

