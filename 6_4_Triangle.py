# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 13:40:33 2020

@author: andya
"""

#triangle


def solution(A):
    
    answer = 0

    if 3 > len(A):
        answer = 0
    else:
        A.sort()
        for i in range(len(A)-2):
            #Q + R > P is given because of sorting
            #R + P > Q is given because of sorting
            if A[i] + A[i+1] > A[i+2]:
                answer = 1
                break
    return answer
        

A = [10,2,5,1,8,20]
solution(A)