# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 11:59:33 2020

@author: andya
"""

def solution(A):

    A.sort()
    
    #large negative * large negative is very large positive
    return max(A[-1] * A[0] * A[1], A[-1] * A[-2] * A[-3])

A = [-3, 1, 2, -2, 5, 6]
solution(A)