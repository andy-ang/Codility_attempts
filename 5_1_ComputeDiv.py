# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 09:24:09 2020

@author: andya
"""

#compute division

A = 6
B = 11

def solution(A, B, K):
    count = 0
    for i in range(A, B+1):
        if i % K == 0:
            count += 1
    return count

solution(6, 10, 2)


# better solution

import math
def solution(A, B, K):
   
    return math.floor(B/K) - math.ceil(A/K) + 1

solution(6, 10, 2)


