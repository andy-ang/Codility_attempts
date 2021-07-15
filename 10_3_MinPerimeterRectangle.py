# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 17:33:33 2021

@author: andya
"""

N = 30


def solution(N):
    
    min_peri = -1
    for a, b in itertools.combinations_with_replacement(list(range(1,N+1)),2):
        if a * b == N:
            curr_peri = 2 * (a + b)
            if min_peri == -1:
                min_peri = curr_peri
            elif min_peri > curr_peri:
                min_peri = curr_peri
                
            
    return min_peri

solution(30)