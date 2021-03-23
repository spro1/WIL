"""
    Date : 2021-03-24
    Source : https://programmers.co.kr/learn/courses/30/lessons/42578
"""
def solution(clothes):
    answer = 1
    dic = {}
    for i in clothes:
        if i[0] not in dic:
            if i[1] in dic.keys():
                values = dic[i[1]]
                values.append(i[0])
                dic[i[1]] = values
            else:
                values = []
                values.append(i[0])
                dic[i[1]] = values

    for v in dic.values():
        answer *= (len(v) + 1)
    return answer - 1