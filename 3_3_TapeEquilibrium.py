# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 15:51:57 2020

@author: andya
"""

#tape_equilibrium
import random
A = [random.randint(0,10) for i in range(10000)]

def solution(A):
    tot_sum = sum(A)
    min_diff = float('inf')
    left_sum = 0
    for i in A[:-1]:
        left_sum += i
        min_diff = min(min_diff, abs(tot_sum - left_sum - left_sum))
    return min_diff

solution(A)