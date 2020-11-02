# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 15:26:44 2020

@author: andya
"""

#find missing element


def solution(A):

    if A == []:
        answer = 1
    elif type(A) != list:
        answer = A
    else:
        sorted_A = sorted(A)
        
        for i in range(len(sorted_A)):
            if sorted_A[i] != i+1:
                answer = i+1
                break
            else:
                answer = i+2
        
    return answer