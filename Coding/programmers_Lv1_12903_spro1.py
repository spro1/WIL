"""
    Date: 2022-05-11
    Source: https://programmers.co.kr/learn/courses/30/lessons/12903
"""

def solution(s):
    print(len(s))
    if len(s)%2==1:
        return s[len(s)//2]
    else: 
        return s[len(s)//2-1:len(s)//2+1]
    return answer