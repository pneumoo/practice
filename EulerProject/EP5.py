# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 13:27:18 2015
@author: Brian
"""

"""
Smallest multiple
Problem 5
2520 is the smallest number that can be divided by each of the 
numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible 
by all of the numbers from 1 to 20?
"""


#==============================================================================
# My solution  (BAD!)
#==============================================================================

'''
num = 20
i = 1
val = num

while i != num:
    if val%i == 0:
        i += 1
    else:
        i = 1        
        val += 1

print(val)
  '''  

            

        

#==============================================================================
# Euler Project Solution:
# REALLY COOL prime factorization method...
#==============================================================================
import math
import time

s = time.time()
primeList=[]
k=20
check=True
limit = k**0.5
N=1

def prime_list(k):
	for i in range(2,k):
		flag=0
		for j in range(i-1,1,-1):			
			if(i%j==0):
				flag=1
		if(flag==0):
			primeList.append(i)

prime_list(k)	

a=[1 for x in range(len(primeList))]

i=0
for item in primeList:
	a[i]=1
	if(check==True):
		if(item<=limit):
			a[i]=math.floor(math.log(k)/math.log(primeList[i]))
		else:			
			check = False	
	N=N*(item**a[i])
	i=i+1	

print(N)


t = time.time() - s
print("Seconds: %s" % t)
