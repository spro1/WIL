"""
    Date: 2022-05-14
    Source: https://programmers.co.kr/learn/courses/30/lessons/82612
"""
def solution(price, money, count):
    answer = 0
    for i in range(count):
        answer += (price*(i+1))

    return answer-money if answer-money > 0 else 0