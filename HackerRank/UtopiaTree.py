# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 20:36:42 2015

@author: Brian
"""

def treeheight(cycles):
    height = 1
    if cycles != 0:
        for i in range(cycles):
            if i%2 == 0:
                height = 2*height
            else:
                height += 1
    return(height)
    
N=10
height = treeheight(N)
print(height)