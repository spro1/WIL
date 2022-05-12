"""
    Date: 2022-05-12
    Source: https://programmers.co.kr/learn/courses/30/lessons/17682
"""

def solution(dartResult):
    dartResult = list(dartResult)
    result = []
    while len(dartResult)!=0:
        num = ''
        q = dartResult.pop(0)
        
        if ord(q) == 35:
            index = len(result)
            result[index-1] *= -1
        elif ord(q) == 42:
            index = len(result)
            if index == 1:
                result[index-1] *= 2
            else:
                result[index-1] *= 2
                result[index-2] *= 2
        else:
            while ord(q) >= 48 and ord(q) <= 57:
                num += q
                q = dartResult.pop(0)
            
            num = int(num)
            
            if q == "S":
                num **= 1
            elif q == "D":
                num **= 2
            elif q == "T":
                num **= 3
            result.append(num)   
    
    return sum(result)