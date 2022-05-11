"""
    Date: 2022-05-11
    Source: https://programmers.co.kr/learn/courses/30/lessons/92334
"""

def solution(id_list, report, k):
    report = list(set(report))
    answer = []
    reporter = {}
    result = {}
    for i in id_list:
        reporter.setdefault(i, [])
        result.setdefault(i, 0)
    
    for i in report:
        r1, r2 = i.split(" ")
        reporter[r1].append(r2)
        result[r2] += 1
    
    for i in id_list:
        user = 0
        for l in reporter[i]:
            if result[l] >= k:
                user += 1
        answer.append(user)
        
    print(answer)
    return answer