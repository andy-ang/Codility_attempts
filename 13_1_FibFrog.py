# -*- coding: utf-8 -*-
"""
Created on Sun Jul 11 14:43:33 2021

@author: andya
"""

def gen_fib_seq(num):

    fib_seq = [0,1]    
    end_loop = 0
    i=2
    while(end_loop==0):
        
        fib_seq.append(fib_seq[i-1] + fib_seq[i-2])
        i+=1
            
        if fib_seq[i-1] + fib_seq[i-2] > num:
            end_loop=1

    return list(set(fib_seq))[1:]

def solution(A):
    #change A to positon
    # A = []
    new_A = []
    for i, j in enumerate(A):
        if j == 1:
            new_A.append(i+1)
    new_A.append(len(A)+1)
    
    #get max fib
    fib_seq = gen_fib_seq(len(A)+1)
       
    end_loop = 0
    jumps = 0
    while(end_loop==0):
        curr_x = 0
        find = 0
        for i in reversed(new_A):
            for j in reversed(fib_seq):
                # print(i,j, i/j)
                if i/j == 1:
                    curr_x = j
                    find = 1
                    break
            if find == 1:
                find = 0
                break
            
        if curr_x > 0:
            # print(curr_x, new_A)
            jumps+=1
            new_A = [x-curr_x for x in new_A if x > curr_x]
          
        else:
            end_loop=1
    
    if jumps == 0 or len(new_A) > 0:
        jumps = -1

    return jumps

A = [0, 0
     0
     ]
solution(A)

    
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        