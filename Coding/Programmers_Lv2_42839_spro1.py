"""
    Date : 2021-04-06
    Source : https://programmers.co.kr/learn/courses/30/lessons/42839
"""
import itertools
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            return False
    return True

def solution(numbers):
    answer = 0
    nums = []
    for i in range(len(numbers)):
        nums += list(map(''.join, itertools.permutations(numbers, i+1)))
    nums = list(set([int(x) for x in nums]))
    for i in nums:
        if is_prime(int(i)):
            answer += 1
            
    return answer