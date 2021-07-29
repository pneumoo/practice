# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 19:29:29 2015

@author: Brian
"""

from random import randint
import heapq

#def mergeSort(alist):
#    if len(alist)>1:
#        mid = len(alist)//2
#        lefthalf = alist[:mid]
#        righthalf = alist[mid:]
#
#        mergeSort(lefthalf)
#        mergeSort(righthalf)
#
#        i=0
#        j=0
#        k=0
#        while i<len(lefthalf) and j<len(righthalf):
#            if lefthalf[i]<righthalf[j]:
#                alist[k]=lefthalf[i]
#                i=i+1
#            else:
#                alist[k]=righthalf[j]
#                j=j+1
#            k=k+1
#
#        while i<len(lefthalf):
#            alist[k]=lefthalf[i]
#            i=i+1
#            k=k+1
#
#        while j<len(righthalf):
#            alist[k]=righthalf[j]
#            j=j+1
#            k=k+1


#def quicksort(alist):
#    less = []
#    equal = []
#    greater = []
#
#    if len(alist) > 1:
#        pivot = alist[0]
#        for x in alist:
#            if x < pivot:
#                less.append(x)
#            if x == pivot:
#                equal.append(x)
#            if x > pivot:
#                greater.append(x)
#        # Don't forget to return something!
#        return sort(less)+equal+sort(greater)  # Just use the + operator to join lists
#    # Note that you want equal ^^^^^ not pivot
#    else:  # You need to hande the part at the end of the recursion - when you only have one element in your array, just return the array.
#        return array

def builtinsort(li):
    li.sort()
    return(li)
    
def heapsort(iterable):
    h = []
    for value in iterable:
        heapq.heappush(h, value)
    return [heapq.heappop(h) for i in range(len(h))]
    


amax = 1000000
A = [randint(0,amax) for p in range(0,amax)]
B = list(A)



builtinsort(A)

heapsort(B)


