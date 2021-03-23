"""
    Date : 2021-03-24
    Source : https://programmers.co.kr/learn/courses/30/lessons/42577
"""
def solution(phone_book):
    answer = True
    diction = sorted(phone_book)
    for i in range(0,len(diction)):
        if i == len(diction)-1:
            break
        if (diction[i] == diction[i+1][0:len(diction[i])]):
            return False
    return answer