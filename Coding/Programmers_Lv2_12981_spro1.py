"""
    Date: 2022-05-20
    Source: https://programmers.co.kr/learn/courses/30/lessons/12981
"""
def solution(n, words):
    answer = []
    number = 1
    count = 1
    before_word = ""
    before_words = []
    while len(words)!=0:
        word = words.pop(0)
        if before_word!="" and word[0] != before_word[-1]:
            return [number, count]
        elif word in before_words:
            return [number, count]
        else:
            before_words.append(word)
        number += 1
        before_word = word
        if number > n:
            number = 1
            count += 1
                
    return [0, 0]