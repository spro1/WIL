"""
    Date: 2022-06-30
    Source: https://programmers.co.kr/learn/courses/30/lessons/12977
"""
import itertools
def solution(nums):
    answer = 0
    nums = list(map(list, itertools.combinations(nums,3)))
    for i in nums:
        num = sum(i)
        for l in range(2, num):
            if num%l == 0:
                break
        else:
            answer += 1
    
    return answer