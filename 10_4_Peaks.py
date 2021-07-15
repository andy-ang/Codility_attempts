# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 22:30:12 2021

@author: andya
"""

def solution(A):
   
    peak_loc = []
    for i in range(len(A)-2):
        if A[i] < A[i+1] and A[i+1] > A[i+2]:
            peak_loc.append(i+1)
    
    max_block = 0
    for i in range(len(A)+1,0,-1):
        if len(A)%i == 0:
            temp_max_block = int(len(A)/i)
            temp_peak = 0
            
            if len(peak_loc) > max_block:
                for j in range(0, len(A), i):
                        for k in peak_loc:
                            if j <= k <= j+i:
                                temp_peak += 1
            if temp_peak == temp_max_block:
                max_block = temp_max_block
    return max_block
                       
