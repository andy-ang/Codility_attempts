# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 12:12:19 2020

@author: andya
"""


def solution(A):
    
    count=0
    for i, j in enumerate(A):
        min_outer = i-j
        max_outer = i+j
        
        for k , l in enumerate(A[i+1:]):
            min_inner = k-l+i+1
            max_inner = k+l+i+1
            
            if min(min_inner, max_inner) > max(min_outer, max_outer) or max(min_inner, max_inner) < min(min_outer, max_outer):
                continue
            else: count+=1
    return count


solution([1,5,2,1,4,0])
           
      
        
    