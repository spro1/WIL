"""
    Date: 2022-05-12
    Source: https://programmers.co.kr/learn/courses/30/lessons/77484
"""
def solution(lottos, win_nums):
    min = set(lottos) & set(win_nums)
    max = len(min) + lottos.count(0)
    
    min = 7-len(min) if len(min)>=2 else 6
    max = 7-max if max>=2 else 6
    answer = [max, min]
    return answer