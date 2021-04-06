"""
    Date : 2021-04-07
    Source : https://programmers.co.kr/learn/courses/30/lessons/42627
    비고 : 소요시간과 시작시간에 대해 우선순위 공부필요
"""
import heapq


def solution(jobs):
    answer = 0
    start = -1
    now = 0
    i = 0
    jobs.sort()
    hq = []

    while i < len(jobs):
        for k, v in jobs:
            if start < k <= now:
                heapq.heappush(hq, [v, k])
        if len(hq) != 0:
            value = heapq.heappop(hq)
            start = now
            now += value[0]
            answer += (now - value[1])
            i += 1
        else:
            now += 1
    return answer // len(jobs)