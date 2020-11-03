# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 22:05:22 2020

@author: andya
"""

def count_in_list(half_A):
    count_dict = dict((x,0) for x in list(set(half_A)))
    for x, y in enumerate(half_A):
            count_dict[y] += 1
    return [max(count_dict, key=count_dict.get), max(count_dict.values())]

def solution(A):
    
    leader = 0
    for i, j in enumerate(A):
        if i>0:
            
            first_half = A[0:i]
            second_half = A[i:]
            
            first_half_res = count_in_list(first_half)
            second_half_res = count_in_list(second_half)
            
            if first_half_res[0] == second_half_res[0] and first_half_res[1] > len(first_half)/2 \
                and second_half_res[1] > len(second_half)/2:
                leader += 1
                
    return leader
                    