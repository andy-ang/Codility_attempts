# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 15:44:08 2021

@author: andya
"""

A = [23171, 21011, 21123, 21366, 21013, 21367]

import itertools

def solution(A):
    max_profit = 0
    for a, b in itertools.combinations(list(range(0,len(A))), 2):
        if 0 <= a < b < len(A):
            curr_profit = A[b] - A[a]
            if curr_profit > max_profit:
                    max_profit = curr_profit
    return max_profit

solution(A)
     