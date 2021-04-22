"""
    Date : 2021-04-22
    Source : https://programmers.co.kr/learn/courses/30/lessons/12982
"""
def solution(d, budget):
    answer = 0
    d.sort()
    for i in d:
        budget -= i
        if budget >= 0:
            answer += 1
        else:
            break
    return answer