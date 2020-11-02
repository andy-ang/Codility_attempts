# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 16:46:29 2020

@author: andya
"""

# get frog across river / FrogRiverOne
A = [1,3,1,4,2,3,5,4]
X = 5

def solution(X, A):
    
    #sort list with index, create distinct
    unique_data = dict([(i[1],i[0]) for i in sorted(enumerate(A), key=lambda x: (x[1], x[0]), reverse=True)])
    
    if A == [] or type(A) != list or len(unique_data) < len(range(1,X+1)):
        answer = -1

    else:
        answer = max(unique_data.values())

    return answer


solution(5, A)
solution(100, A)


A = [1,3,1,4,2,3,5,4]
B = [0,1,2,3,4,5,6,7]
c = [A,B]

# sort by values
K= sorted(zip(A,B), key=lambda x: (x[0], x[1]), reverse=True)

