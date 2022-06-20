"""
    Date: 2022-06-20
    Source: https://programmers.co.kr/learn/courses/30/lessons/77884
"""
def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        count = 0
        for l in range(1, i+1):
            if i%l == 0:
                count += 1
        if count%2==0:
            answer += i
        else:
            answer -= i
    return answer