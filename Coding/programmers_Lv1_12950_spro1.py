"""
    Date: 2022-05-19
    Source: https://programmers.co.kr/learn/courses/30/lessons/12950
"""
def solution(arr1, arr2):
    answer = []
    for i, l in zip(arr1, arr2):
        value = []
        for a, b in zip(i, l):
            value.append(a+b)
        answer.append(value)
        
    return answer