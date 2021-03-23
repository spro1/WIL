"""
    Date : 2021-03-10
    Source : https://programmers.co.kr/learn/courses/30/lessons/72410
"""
import re
def solution(new_id):
    answer = ''
    # 1단계 대문자 -> 소문자
    answer = new_id.lower()
    # 2단계 특수 문자 제거
    answer = re.sub('[^a-zA-Z0-9.\-_]','', answer)
    # 3단계 .. -> .
    answer = re.sub('\.{2,}','.',answer)
    # 4단계 처음과 끝 . 제거
    answer = (answer.lstrip(".")).rstrip(".")
    # 5단계 빈 문자열
    if answer == "":
        answer = "a"
    # 6단계 16자 이상이면 15개로 줄이기, 마지막이 마침표면 삭제
    if len(answer) > 15:
        answer = answer[:15]
        while answer[-1]==".":
            answer = answer.rstrip(".")
    # 7단계 2자 이하라면 마지막 문자 반복
    while(len(answer)<3):
        answer = answer+answer[-1]
    return answer