"""
    Date: 2022-05-19
    Source: https://programmers.co.kr/learn/courses/30/lessons/81301
"""
def solution(s):
    answer = ''
    dic = {'zero':'0', 'one':'1','two':'2', 'three':'3', 'four':'4', 'five':'5',
          'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}
    
    word = ""
    for i in s:
        if ord(i)>96 and ord(i)<123:
            word += i
            if word in dic:
                answer += dic[word]
                word = ""
        else:
            answer += i
    return int(answer)