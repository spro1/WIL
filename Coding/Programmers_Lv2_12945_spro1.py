"""
    Date: 2022-06-30
    Source: https://programmers.co.kr/learn/courses/30/lessons/12945
"""
def fib(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
    
def fib2(n):
    _curr, _next = 0, 1
    for _ in range(n):
        _curr, _next = _next, _curr + _next
    return _curr

def solution(n):
    answer = 0

    return fib2(n)%1234567