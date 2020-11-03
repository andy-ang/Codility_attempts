# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 21:07:21 2020

@author: andya
"""

def solution(A):
    
    if A == []:
        answer = -1
    else:
        unique_index_dict = dict((x,-1) for x in list(set(A)))
        count_dict = dict((x,0) for x in list(set(A)))
        
        for i, j in enumerate(A):
            if unique_index_dict[j] == -1:
                unique_index_dict[j] = i
            count_dict[j] += 1
        
        max(count_dict.values())
        if max(count_dict.values()) > len(A)/2:
            answer = unique_index_dict[max(count_dict, key=count_dict.get)]
        else: 
            answer = -1
            
    return answer

solution([])
solution([3,4,3,2,3,-1,3,3])