"""
    Date: 2022-05-12
    Source: https://programmers.co.kr/learn/courses/30/lessons/60057
"""
def solution(s):
    answer = []
    if len(s) == 1:
        return 1
    for n in range(int(len(s)/2)):
        ss = [s[i:i+n+1] for i in range(0, len(s), n+1)]
        count = 1
        word = ss.pop(0)
        new_ss = ""
        while len(ss) > 0:
            next_word = ss.pop(0)
            if word == next_word:
                count += 1
                word = next_word
            else:
                if count <= 1:
                    new_ss += word
                else:
                    new_ss += (str(count)+word)
                count = 1
                word = next_word
        if count <= 1:
            new_ss += word
        else:
            new_ss += (str(count)+word)
        answer.append(len(new_ss))
    return min(answer)