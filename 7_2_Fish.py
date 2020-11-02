# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 21:49:28 2020

@author: andya
"""

def solution(A, B):
        
    # 0,1 -> wont meet
    # 1,0 -> meet
    # 1,1 -> wont meet
    # 0,0 -> wont meet
    
    start_pos = 0
    loop_cont = 1
    while (loop_cont == 1):
        #print(A, B)
        if len(A) == 1:
            loop_cont = 0
        else:
            if B[start_pos] == 1 and B[start_pos+1] == 0:
                if A[start_pos] > A[start_pos+1]:
                    A.pop(start_pos+1)
                    B.pop(start_pos+1)
                      
                else: 
                    A.pop(start_pos)
                    B.pop(start_pos)
                      
            else: 
                start_pos += 1
                
            if start_pos == len(A)-1:
                
                for i in range(len(B)-1):
                    if B[i] == 1 and B[i+1] == 0:
                        print('hello', i)
                        start_pos = 0
                        loop_cont = 1
                        break
                    else: 
                        loop_cont = 0
                
            
    return len(B)            
                    
                
            
