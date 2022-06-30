"""
    Date: 2022-06-30
    Source: https://programmers.co.kr/learn/courses/30/lessons/12953
"""
def gcd (a, b):
    while b > 0:
        a, b = b, a%b
    return a

def lcm (a,b):
    return a * b / gcd(a,b)

def solution(arr):
    answer = 0
    while arr:
        if answer==0:
            answer = arr.pop()
        else:
            answer = lcm(answer, arr.pop())
        
    return answer