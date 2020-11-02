# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 11:23:28 2020

@author: andya
"""

A = [0,1,0,1,1,0,1]
def solution(A):
  
    answer = 0
    for i, j in enumerate(A):
        if j == 0:
            answer += (sum(A[i:]))
    
    if answer > 1000000000:
        answer = -1
        
    return answer



#better solution
def solution(A):
  
    answer = 0
    west_car = 0
    
    for i in A:
        if i == 0:
            west_car += 1
        else:
            answer += west_car
    
    if answer > 1000000000:
        answer = -1
        
    return answer

