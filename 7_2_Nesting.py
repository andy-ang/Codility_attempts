# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 21:00:26 2020

@author: andya
"""


def solution(S):
    new_S = S
    check_brackets = ['()']
    open_loop = 1
    while(open_loop == 1):
        
        end = 0
        found_closed = 0
        if new_S == '':
            break
        
        else:

            if any(ext in new_S for ext in check_brackets):
                new_S = new_S.replace('()', '')
                found_closed = 1
                      
            else: found_closed = 0
                                 
        if found_closed == 0:
            open_loop = 0
             
    if len(new_S) == 0:
        answer = 1
    else: answer = 0
    
    return answer


solution('(()(())())')

solution('())')