"""
    Date : 2021-04-01
    Source : https://programmers.co.kr/learn/courses/30/lessons/42584
"""
from collections import deque
def solution(prices):
    answer = []
    price = deque(prices.copy())
    for i in prices:
        cnt = 0
        price.popleft()
        for l in price:
            if i <= l:
                cnt += 1
            elif i > l:
                cnt += 1
                break
        answer.append(cnt)
    return answer

"""
def solution(prices):
    answer = [0] * len(prices)
    for i in range(len(prices)):
        for l in range(i+1, len(prices)):
            if prices[i] <= prices[l]:
                answer[i] += 1
            else:
                answer[i] += 1
                break
    return answer
"""