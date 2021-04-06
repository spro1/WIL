"""
    Date : 2021-04-06
    Source : https://programmers.co.kr/learn/courses/30/lessons/42579
"""
def solution(genres, plays):
    answer = []
    dic = {}
    for k, v in enumerate(genres):
        if v not in dic.keys():
            dic[v] = [0, []]
        dic[v][0] += plays[k]
        dic[v][1].append((k, plays[k]))
    dic = sorted(dic.items(), key=lambda x: x[1][0])
    
    for k, v in enumerate(dic[::-1]):
        value = sorted(v[1][1], key=lambda x:(x[1], -x[0]))
        if len(value) == 1:
            answer.append(value[0][0])
        else:
            answer.append(value[::-1][0][0])
            answer.append(value[::-1][1][0])
    return answer