'''
    Date : 2021-04-07
    Source : https://programmers.co.kr/learn/courses/30/lessons/42883
'''
def solution(number, k):
    answer = []
    answer_len = len(number)-k
    n = 0
    for i in range(answer_len):
        if len(number) == answer_len-i:
            answer += number
            break
        max_num = "0"
        for i in number[:len(number)-(answer_len-(i+1))]:
            if i=="9":
                max_num="9"
                break
            elif i>max_num:
                max_num = i
        
        num_idx = number.index(max_num)
        number = number[num_idx+1:]
        answer.append(max_num)
    return ''.join(answer)