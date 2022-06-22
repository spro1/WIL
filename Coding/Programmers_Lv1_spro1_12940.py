"""
    Date: 2022-06-22
    Source: https://programmers.co.kr/learn/courses/30/lessons/12940
"""
def solution(n, m):
    max = m*n
     
    while m!=0:
        n, m = m, n%m
    
    min = n
    max /= n
    
    return [min, max]