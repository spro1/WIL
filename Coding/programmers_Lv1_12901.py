"""
    Date : 2021-03-09
    Source : https://programmers.co.kr/learn/courses/30/lessons/12901
"""
def solution(a, b):
    # 월별 일 수
    monthly_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # 해당 이전 월(a-1)까지 합산한 후 해당 b일 합산
    days = sum(monthly_days[:a-1]) + b
    # 1월 1일 금요일 기준 요일 체크
    day_of_weeks = days%7
    if day_of_weeks == 1:
        answer = "FRI"
    elif day_of_weeks == 2:
        answer = "SAT"
    elif day_of_weeks == 3:
        answer = "SUN"
    elif day_of_weeks == 4:
        answer = "MON"
    elif day_of_weeks == 5:
        answer = "TUE"
    elif day_of_weeks == 6:
        answer = "WED"
    else:
        answer = "THU"
    return answer
