# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 14:02:04 2020

@author: andya
"""

# find longest 0
def solution(N):

    bin_N = '{0:08b}'.format(N)
   
    start = 0
    for i in range(len(bin_N)):
        if bin_N[i] == '1':
            start = i
            break
    
    count =0
    longest_0 = 0
    for i in range(start, len(bin_N)):
        
        if bin_N[i] == '0':
            count += 1
        else: 
            
            if longest_0 <= count:
                longest_0 = count
            count = 0
    return longest_0

solution(15)
solution(147)
solution(483)
solution(647)




