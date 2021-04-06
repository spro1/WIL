"""
    Date : 2021-04-06
    Source : https://programmers.co.kr/learn/courses/30/lessons/42587
"""
from collections import deque
def solution(priorities, location):
    answer = 0
    priorities = deque(priorities)
    while len(priorities):
        if priorities[0] < max(priorities):
            v = priorities.popleft()
            priorities.append(v)
            if location == 0:
                location = len(priorities)-1
            else:
                location -= 1
        else:
            priorities.popleft()
            answer += 1
            if location == 0:
                return answer
            else:
                location -= 1
    return answer