"""
    Date: 2022-06-28
    Source: https://programmers.co.kr/learn/courses/30/lessons/12926
"""
def solution(s, n):
    answer = ""
    for i in s:
        i = ord(i)
        if 97<= i <= 122:
            i+= n
            if i>122:
                i-=26
        elif 65<= i <= 90:
            i+= n
            if i>90:
                i-=26
        answer += chr(i)
    
    return answer