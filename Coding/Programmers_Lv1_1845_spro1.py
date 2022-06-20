"""
    Date: 2022-06-20
    Source : https://programmers.co.kr/learn/courses/30/lessons/1845
"""
def solution(nums):
    return len(list(set(nums))) if len(nums)/2 > len(list(set(nums))) else len(nums)/2