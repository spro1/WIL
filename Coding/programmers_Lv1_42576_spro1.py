"""
    Date : 2021-03-23
    Source : https://programmers.co.kr/learn/courses/30/lessons/42576
"""
def solution(participant, completion):
    dict = {}
    for i in participant:
        if i not in dict:
            dict[i] = 0
        else:
            dict[i] = dict.get(i) + 1
    for l in completion:
        if l in dict:
            dict[l] = dict.get(l) - 1

    return list(dict.keys())[list(dict.values()).index(0)]