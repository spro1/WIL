"""
    Date: 2022-05-19
    Source: https://programmers.co.kr/learn/courses/30/lessons/12932
"""
def solution(n):
    answer = [int(i) for i in list(str(n))]
    answer.reverse()
    return answer