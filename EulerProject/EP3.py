# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 13:27:18 2015
@author: Brian
"""

"""
Largest prime factor
Problem 3
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the 
number 600851475143 ?
"""


#==============================================================================
# My solution  
#==============================================================================

import time
s = time.time()
    
def largestprimefactor(n):
    n=int(n)                                        #make sure input is an integer
    a=int(n**0.5)                                   #sqrt(n) is largest possible factor       

    while(1 <= a):                                  #count down from a, since we're looking for biggest prime factor
        b=a                                         #use b for loop internals
        
        if n%b == 0 and a != 1:                     #b is a factor of n AND b isn't equal to 1
            for i in range(2,b+1):                  #for loop to determine if b is prime or not
                if b%i == 0 and i != b:             #if i is a factor of b, b is not prime
                    a -= 1                          #decrement a, since it is not prime
                    break                           #go back to while loop
                elif i == b:                        #if i searches up to b without being eliminated then b is prime
                    a = 0                           #set a=0 to break the while loop     
                    break                           #go back to while loop
        
        elif b == 1:                                #if b gets to 1, then n is prime
            return(print("that number is prime"))   #notify the user that n is prime
        
        else:                                       #if b is not a factor of n, decrement a
            a -= 1                                  #decrement a, since it is not prime
    
    return(b)                                       #return b, since it is now the largestprimefactor
        

print(largestprimefactor(600851475143))
t = time.time() - s
print("Seconds: %s" % t)

#==============================================================================
# Euler Project Solution:
#==============================================================================
