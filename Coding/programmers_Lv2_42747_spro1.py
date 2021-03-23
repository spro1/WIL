"""
    Date : 2021-03-24
    Source : https://programmers.co.kr/learn/courses/30/lessons/42747
"""
def solution(citations):
    answer = 0
    n = len(citations)
    citations = sorted(citations)
    for i in range(n):
        print(citations[i], n)
        if citations[i] >= n-i:
            return n-i
    return answer