"""
    Date : 2021-03-11
    Source : https://programmers.co.kr/learn/courses/30/lessons/12899
"""
def solution(n):
    answer = ''
    while n>0:
        n, y = n//3, n%3
        if y == 0:
            y=4
            n-=1
        answer = str(y) + answer
    return answer
