"""
    Date : 2021-03-11
    Source : https://programmers.co.kr/learn/courses/30/lessons/68935
"""
def re(num):
    q, r = divmod(num, 3)
    r = str(r)
    return re(q) + r if q else r

def solution(n):
    answer = int(''.join(reversed(re(n))), 3)
    return answer