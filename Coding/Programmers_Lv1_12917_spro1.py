"""
    Date: 2022-06-29
    Source: https://programmers.co.kr/learn/courses/30/lessons/12917
"""
def solution(s):
    s = list(s)
    s.sort()
    s.reverse()
    return "".join(s)