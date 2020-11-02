# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 09:45:08 2020

@author: andya
"""



def solution(S, P, Q):
      
    map_dict = dict({'A' : 1,'C': 2, 'G': 3, 'T':4})
 
    answer = []
    for pq in range(len(P)):
   
        used = []
        [used.append(x) for x in S[P[pq]:Q[pq]+1] if x not in used]
        unique_pq = ''.join(used)
        
        if unique_pq == '':
            answer.append(0)
        else:
            min_S = 100
            for i in unique_pq:
                if min_S >= map_dict.get(i):
                    min_S = map_dict.get(i)
            answer.append(min_S)
    return answer
        