"""
    Date: 2022-05-19
    Source: https://programmers.co.kr/learn/courses/30/lessons/12928
"""
def solution(n):
    answer = 0
    for i in range(1, n+1):
        if n%i == 0:
            answer += i
    return answer