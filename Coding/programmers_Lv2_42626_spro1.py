"""
    Date : 2021-03-29
    Source : https://programmers.co.kr/learn/courses/30/lessons/42626
"""
def solution(scoville, K):
    import heapq
    answer = 0
    heapq.heapify(scoville)
    while 1:
        if scoville[0] >= K:
            break
        if len(scoville) == 1:
            return -1
        heapq.heappush(scoville, heapq.heappop(scoville) + (heapq.heappop(scoville) * 2))
        answer += 1
    return answer
