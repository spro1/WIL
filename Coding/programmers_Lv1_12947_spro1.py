"""
    Date: 2022-05-19
    Source: https://programmers.co.kr/learn/courses/30/lessons/12947
"""
def solution(x):
    sum = 0
    for i in list(str(x)):
        sum += int(i)
    
    return True if x%sum==0 else False