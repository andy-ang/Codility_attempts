# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 14:35:23 2021

@author: andya
"""


A = [-3,-2,-6,-1,-4,-5,-1,-2]

import itertools

def solution(A):
    max_double_slice = 0
    for a, b, c in itertools.combinations(list(range(0,len(A))), 3):
        if 0 <= a < b < c < len(A):
            double_slice = sum(A[a+1:b]) + sum(A[b+1:c])
            if double_slice > max_double_slice:
                    max_double_slice = double_slice
    return max_double_slice
                
            
solution(A)