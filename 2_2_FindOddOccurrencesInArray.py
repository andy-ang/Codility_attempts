# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 15:01:37 2020

@author: andya
"""

## get unpaired element

import collections
def solution(A):
    
    counter = collections.Counter(A)
    for item in counter.items():
        if item[1] % 2 != 0:
            results = item[0]

    return results
    
solution([9,3,9,3,9,7,9,9,3,9,3,9,9,3,9,3,9,9,3,9,3,9,9,3,9,
          3,9,9,3,9,3,9,9,3,9,3,9,9,3,9,3,9,9,3,9,3,9,9,3,9,3,9,9,3,9,3,9,9,3,9,3,9,9,3,9,3,9,9,3,9,3,9])


A = [9,3,9,3,9,7,9]

A[0]