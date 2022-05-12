"""
    Date: 2022-05-12
    Source: https://programmers.co.kr/learn/courses/30/lessons/17677
"""
import math
def solution(str1, str2):
    answer = 0
    str1_list = []
    str2_list = []
    for i in range(0, len(str1), 1):
        word = ""
        for l in str1[i:i+2].upper():
            if ord(l)>=65 and ord(l)<=90:
                word += l
        if len(word) == 2:
            str1_list.append(word)
            
    for i in range(0, len(str2), 1):
        word = ""
        for l in str2[i:i+2].upper():
            if ord(l)>=65 and ord(l)<=90:
                word += l
        if len(word) == 2:
            str2_list.append(word)
        
    union1 = str1_list.copy()
    union = str1_list.copy()
    for i in str2_list:
        union.append(i) if i not in union1 else union1.remove(i)
    
    print(union)
    
    intersection = []
    for i in str2_list:
        if i in str1_list: str1_list.remove(i); intersection.append(i)

    print(intersection)
    
    if len(intersection) == len(union):
        return 65536
    answer = (len(intersection) / len(union) * 65536)
    
    return math.trunc(answer)