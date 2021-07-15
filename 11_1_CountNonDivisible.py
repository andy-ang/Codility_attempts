# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 23:36:20 2021

@author: andya
"""

A = [3,1,2,3,6]


def solution(A):
    answer = []
    for i in range(len(A)):
        answer.append(len(A) - len([x for x in A if A[i]%x == 0]))
    return answer


solution(A)