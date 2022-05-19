"""
    Date: 2022-05-19
    Source: https://programmers.co.kr/learn/courses/30/lessons/12930
"""
def solution(s):
    answer = ''
    for i in s.split(" "):
        for l, j in enumerate(i):
            if(l%2==0):
                j = j.upper()
            else:
                j = j.lower()
            answer+=j
        answer += " "
    return answer[:-1]