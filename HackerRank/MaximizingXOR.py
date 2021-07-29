# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 20:36:42 2015

@author: Brian

This finds the largest XORed value of any combination of two numbers,
l and r. The loops .pop() off the 1st value from rlist each time so that
duplicate combinations aren't executed - this should cut running time by
about half. Another trick is that any value XORed by iself is 0, so we
don't need to check those, as max = 0 already. 

"""


def maxXor(l, r):
    max = 0
    llist = list(range(l,r+1))
    rlist = list(range(l,r+1))

    for i in range(r-l):
        for j in range(len(rlist)):
            if llist[i] != rlist[j]:
                a = llist[i] ^ rlist[j]
#                print(llist)
#                print(rlist)
#                print(llist[i], rlist[j], a)
                if a > max:
                    max = a
        rlist.pop(0)  
    return(max)
    

if __name__ == '__main__':
  l = int(input())
  r = int(input())
  print(maxXor(l, r))