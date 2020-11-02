# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 10:46:10 2020

@author: andya
"""

def solution(A):

    avges = float()
    avg_position = int()
    
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            
            temp_avg = sum(A[i:j+1])/(j+1-i)
            if i == 0 and j == 1:
                avges = temp_avg
                avg_position = i
                
            elif avges == temp_avg:
                if avg_position > i:
                    avg_position = i

            elif avges > temp_avg:
                avges = temp_avg
                avg_position = i
                
    return avg_position

        
    