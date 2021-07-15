# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 18:11:53 2021

@author: andya
"""

N = 10
M = 4

def solution(N, M):
    
    list_N = list(range(N))
    answer = [0]
    wrapper_exists = 0
    i = 0
    while (wrapper_exists == 0):
        
        if list_N[(i+M)%N] in answer:
            wrapper_exists = 1
        else:
            answer.append(list_N[(i+M)%N])
            i=i+M

        
    return len(answer)