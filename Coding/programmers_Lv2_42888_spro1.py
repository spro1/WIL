"""
    Date: 2022-05-12
    Source: https://programmers.co.kr/learn/courses/30/lessons/42888
"""
def solution(record):
    answer = []
    user = {}
    for i in record:
        i = i.split(" ")
        if(len(i) == 3):
            user[i[1]] = i[2]
    for i in record:
        i = i.split(" ")
        if i[0] == "Enter":
            answer.append("%s님이 들어왔습니다."%(user[i[1]]))
        elif i[0] == "Leave":
            answer.append("%s님이 나갔습니다."%(user[i[1]]))
    return answer