"""
    Date: 2022-05-16
    Source: https://programmers.co.kr/learn/courses/30/lessons/64065
"""
def solution(s):
    answer = []
    new_s = []
    s = s.split('},')
    for i in s:
        i = i.replace("{", "").replace("}", "")
        i = i.split(",")
        new_s.append(i)
    new_s.sort(key=len)
    for i in new_s:
        for l in i:
            if int(l) not in answer:
                answer.append(int(l))
    return answer