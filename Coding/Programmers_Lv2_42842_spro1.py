"""
    Date : 2021-04-06
    Source : https://programmers.co.kr/learn/courses/30/lessons/42842
"""
def solution(brown, yellow):
    answer = []
    squre = []
    count = brown + yellow
    for i in range((count)//2):
        k, v = divmod(count, i+1)
        if v==0:
            if(i+1 >= k):
                
                if (i-1)*(k-2)== yellow:
                    answer.append(i+1)
                    answer.append(k)
                    break
    return answer