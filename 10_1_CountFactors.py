# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 16:19:04 2021

@author: andya
"""


N = 24

def solution(N):
    
    factor_cnt = 0
    
    for i in range(1,N+1):
        if N%i == 0:
            factor_cnt += 1
    
    return factor_cnt

solution(N)