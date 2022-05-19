"""
    Date: 2022-05-19
    Source: https://programmers.co.kr/learn/courses/30/lessons/76501
"""
def solution(absolutes, signs):
    answer = 0
    
    for i, l in enumerate(absolutes):
        if signs[i] == True:
            answer += l
        else:
            answer += -l
    
    return answer