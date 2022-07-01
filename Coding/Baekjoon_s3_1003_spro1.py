"""
    Date: 2022-07-01
    Source: https://www.acmicpc.net/problem/1003
"""

N = int(input())
C = []

for i in range(N):
    C.append(int(input()))

def fibo(n):
    _curr, _next = 0, 1
    for _ in range(n):
        _curr, _next = _next, _curr + _next
    return _curr

for i in C:
    if i == 0:
        print(1, 0)
    else:
        print(fibo(i-1), fibo(i))
