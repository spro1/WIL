"""
    Date: 2022-05-19
    Source: https://programmers.co.kr/learn/courses/30/lessons/12933
"""
def solution(n):
    answer = list(str(n))
    answer.sort(reverse=True)
    return int("".join(answer))