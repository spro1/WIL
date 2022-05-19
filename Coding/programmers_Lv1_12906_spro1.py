"""
    Date: 2022-05-19
    Source: https://programmers.co.kr/learn/courses/30/lessons/12906
"""
def solution(arr):
    answer = []
    for i in arr:
        if len(answer) == 0:
            answer.append(i)
        else:
            if i != answer[-1]:
                answer.append(i)
    
    return answer