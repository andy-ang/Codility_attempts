# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 15:54:28 2021

@author: andya
"""


A = [-2,-10]
import itertools

def solution(A):
    max_sum = -9999999999999999999999999999999999999999
    for a, b in itertools.combinations_with_replacement(list(range(0,len(A))),2):
        if 0 <= a <= b < len(A):
            if len(A[a:b+1]) > 0:
                curr_sum = sum(A[a:b+1])
                if curr_sum > max_sum:
                        max_sum = curr_sum
    return max_sum

solution(A)