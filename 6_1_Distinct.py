# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 11:45:59 2020

@author: andya
"""

def solution(A):
    answer = []
    [answer.append(x) for x in A if x not in answer]
    return len(answer)

solution([2,1,1,2,3,1])




#better solution
def solution(A):
    if len(A) == 0:
        distinct_answer = 0
    else:
        distinct_answer = 1
        A.sort()
        for i in range(1, len(A)):
            if A[i] == A[i-1]:
                # The same element as the previous one
                continue
            else:
                # A new element
                distinct_answer += 1
    return distinct_answer