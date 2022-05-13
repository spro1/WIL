"""
    Date : 2022-05-14
    Source : https://programmers.co.kr/learn/courses/30/lessons/12973
"""
def solution(s):
    stack = []
    for i in s:
        if stack:
            if stack[-1] == i:
                stack.pop()
            else:
                stack.append(i)
        else:
            stack.append(i)

    if stack:
        return 0
    else:
        return 1