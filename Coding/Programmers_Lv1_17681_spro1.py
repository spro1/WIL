"""
    Date: 2022-06-29
    Source: https://programmers.co.kr/learn/courses/30/lessons/17681
"""
def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        bin = format(arr1[i]|arr2[i],'b')
        if len(bin) < n:
            bin = ("0"*(n-len(bin)))+bin
        bin = bin.replace("0", " ").replace("1", "#")
        answer.append(bin)
    return answer