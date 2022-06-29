"""
    Date: 2022-06-29
    Source: https://programmers.co.kr/learn/courses/30/lessons/12921
"""
def solution(n):
    prime = [True for i in range(1, n+1)]
    prime[0] = False
    for i in range(2, n+1):
        if(prime[i-1]):
            for l in range(i+i, n+1, i):
                prime[l-1]=False
    
    return prime.count(True)