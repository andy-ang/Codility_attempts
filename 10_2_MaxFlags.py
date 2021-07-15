# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 23:17:35 2021

@author: andya
"""



A = [1,5,3,4,3,4,1,2,3,4,6,2]
def solution(A):
   
    peak_loc = []
    for i in range(len(A)-2):
        if A[i] < A[i+1] and A[i+1] > A[i+2]:
            peak_loc.append(i+1)
    
    max_flag = 1
    for j in range(len(peak_loc), 1, -1):
        
        j = 3
        temp_flag = 0
        for k in range(len(peak_loc)-1):
            if (abs(peak_loc[k] - peak_loc[k+1])) >= j:
                temp_flag += 1
            
    
        if temp_flag >= j:
            max_flag = j