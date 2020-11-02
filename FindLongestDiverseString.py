# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 14:38:45 2020

@author: andya
"""

def create_list_of_substring(X, output_string):
    
    sub_A = []
    temp_A = ''
    count = 0
    if X == 1:
        sub_A.append(output_string)

    else:
        for i in range(X):
            temp_A += output_string
            count += 1
            if count == 2:
                sub_A.append(temp_A)
                count = 0
                temp_A = ''
          
    if X % 2 == 1 and X != 1:
        sub_A.append(output_string)        
           
    return sub_A
          

    
from itertools import permutations
def solution(A, B, C):
    
    listA = create_list_of_substring(A, 'a')
    listB = create_list_of_substring(B, 'b')
    listC = create_list_of_substring(C, 'c')
    
    final_perm_list = []
    
    #generate all permutations of lists
    for i in list(permutations(listA + listB + listC)):
        perm_list = []
        #remove entries that are similar side by side
        for j in range(len(i)):
            if j == 0:
                perm_list.append(i[0])
            elif i[j-1] != i[j]:
                perm_list.append(i[j])
                
        if len(perm_list) >= 2 and perm_list[0] == perm_list[1]:
            perm_list.pop(0)
            
        final_perm_list.append(perm_list)
    
    
    answer = []
 
    for i in final_perm_list:
        if not ('ccc' and 'aaa' and 'bbb')  in ''.join(i):
            answer.append(''.join(i))
    
    if answer == []:
        answer = ''
    else:
        answer = max(answer, key=len)

    return answer

solution(0, 1, 8)
solution(1, 3, 1)
solution(6, 1, 1)
    










           
def solution(A, B, C):
    
    A = 6
    B = 1
    C = 1
    
    listA = create_list_of_substring(A, 'a')
    listB = create_list_of_substring(B, 'b')
    listC = create_list_of_substring(C, 'c')
    
    answer = ['z']

    count = 0
    while(count < 6):
        previous_answer = len(answer)

        if  listA != [] and answer[-1][0] != listA[0][0]:
            answer.append(listA[0]) 
            listA.pop(0)
            
        if listB != [] and answer[-1][0] != listB[0][0]:
            answer.append(listB[0]) 
            listB.pop(0)
        
        if listC != [] and answer[-1][0] != listC[0][0] :
            answer.append(listC[0])
            listC.pop(0)
            
        if  listA != [] and answer[1][0] != listA[0][0]:
            #answer.append(listA[0]) 
            answer.insert(1,listA[0])
            listA.pop(0)
            
        if listB != [] and answer[1][0] != listB[0][0]:
            #answer.append(listB[0]) 
            answer.insert(1,listB[0])
            listB.pop(0)
        
        if listC != [] and answer[1][0] != listC[0][0] :
            #answer.append(listC[0])
            answer.insert(1,listC[0])
            listC.pop(0)
        
        if previous_answer == len(answer):
            count += 1

    return ''.join(answer[1:])


        
        
    