"""
    Date: 2022-05-19
    Source: https://programmers.co.kr/learn/courses/30/lessons/86491
"""
def solution(sizes):
    width = []
    height = []
    for i in sizes:
        width.append(min(i))
        height.append(max(i))
    return max(width) * max(height)