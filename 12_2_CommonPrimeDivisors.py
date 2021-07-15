# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 18:50:21 2021

@author: andya
"""
N = 15
def get_prime_divisor(N):
    prime_list = []
    for i in range(2, N + 1):
        # all prime numbers are greater than 1
        if i > 1 and N%i == 0:
            for j in range(2, i):
                if (i % j) == 0:
                    break
            else:
                prime_list.append(i)
    return prime_list

def solution(A, B):
    
    answer = 0
    for i in range(len(A)):
        A_list = get_prime_divisor(A[i])
        B_list = get_prime_divisor(B[i])
        
        if A_list == B_list:
            answer += 1
    return answer

solution(A,B)