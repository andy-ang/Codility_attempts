# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 18:15:35 2020

@author: andya
"""

# max counters

def solution(N, A):
 
    counters = [0] * N
    
    for X in A:
        if X == N + 1:
            counters = [max(counters)] * N
        elif 1 <= X <= N:
            counters[X-1] += 1

            
    return counters


solution(5, [3,4,4,6,1,4,4])
