# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 22:52:37 2020

@author: andya
"""

#check permutations
A = [1000]
A = [1, 5,4,3,2,1, 6,6,6]
def solution(A):
    min_A = min(A)
    max_A = max(A)
    unique_data = set(A)
    
    answer = 0
    if len(A) > len(unique_data):
        answer = 0
    elif max_A - len(A) == 0:
        answer = 1
    
    return answer

solution([1000000000])
solution([-1,0, 5,4,3,2,1, 6])
