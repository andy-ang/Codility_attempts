# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 18:57:45 2020

@author: andya
"""

A = [4,5,6,2]

def solution(A):

    answer = 0
    pos_A = [x for x in A if x > 0]

    if pos_A == []:
        answer = 1
    else:
        min_A = min(pos_A)
        max_A = max(pos_A)
        unique_data = set(pos_A)
        random_data = set(range(1, max_A+2))
        answer = min(random_data - unique_data)
    return answer

solution(A)
solution([-99999, 1])
solution([-3,-1])
