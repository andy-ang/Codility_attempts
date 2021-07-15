# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 15:27:26 2021

@author: andya
"""

#generate prime and semi prime
def gen_prime(N, start, end):
    prime_list = []

    for i in range(2, N + 1):
        # all prime numbers are greater than 1
        if i > 1:
            for j in range(2, i):
                if (i % j) == 0:
                    break
            else:
                prime_list.append(i)
    
    semi_prime_list = []
    for i in prime_list:
        for j in prime_list:
            if start <= i*j <= end and i*j not in semi_prime_list:
                semi_prime_list.append(i*j)
    
    return len(semi_prime_list)


N = 26
P = [1,4,16]
Q = [26,10,20]

def solution(N, P, Q):
    answer = []
    for i, j in zip(P, Q):
        answer.append(gen_prime(N, i, j))
    return answer