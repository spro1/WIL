"""
    Date: 2022-05-19
    Source: https://programmers.co.kr/learn/courses/30/lessons/12910
"""
def solution(arr, divisor):
    answer = []
    for i in arr:
        if i%divisor == 0:
            answer.append(i)
    answer.sort()
    return answer if len(answer)!=0 else [-1]