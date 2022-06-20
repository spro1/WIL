"""
    Date: 2022-06-20
    Source: https://programmers.co.kr/learn/courses/30/lessons/87389
"""
def solution(n):
    answer = 0
    for i in range(2, n+1):
        if (n%i)==1:
            answer = i
            break
    return answer