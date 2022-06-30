"""
    Date: 2022-06-30
    Source: https://programmers.co.kr/learn/courses/30/lessons/67256
"""
def solution(numbers, hand):
    answer = ''
    left = 10
    right = 12
    for i in numbers:
        if i in [1, 4, 7]:
            answer += "L"
            left = i
        elif i in [3, 6, 9]:
            answer += "R"
            right = i
        else:
            if i == 0:
                i = 11
            left_distance = abs(i-left)//3+abs(i-left)%3 if abs(i-left)%3!=0 else abs(i-left)//3
            right_distance = abs(i-right)//3+abs(i-right)%3 if abs(i-right)%3!=0 else abs(i-right)//3
            if left_distance < right_distance:
                answer += "L"
                left = i
            elif right_distance < left_distance:
                answer += "R"
                right = i
            else:
                if hand == "left":
                    answer += "L"
                    left = i
                else:
                    answer += "R"
                    right = i                
        
    return answer