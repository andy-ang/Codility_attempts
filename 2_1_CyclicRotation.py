# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 14:24:45 2020

@author: andya
"""

#rotating arrays
import numpy as np

def solution(A, K):
    temp_array = A
    if K == 0:
        final_array = A
    if A == []:
        final_array = A
    else:
        for i in range(K):
            final_array = []
            final_array.append(temp_array[-1])
            final_array.extend(temp_array[0:-1])
            temp_array=final_array
    return final_array

solution([3, 8, 9, 7, 6], 3)
solution([], 3)
        
    