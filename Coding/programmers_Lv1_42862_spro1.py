"""
    Date : 2021-04-07
    Source : https://programmers.co.kr/learn/courses/30/lessons/42862

"""

def solution(n, lost, reserve):
    student = [1 for _ in range(n)]
    for i in lost:
        student[i-1] -= 1
    for i in reserve:
        student[i-1] += 1
        
    for n in range(len(student)):
        if student[n] == 2:
            if n==0:
                if student[n+1] == 0:
                    student[n+1]+=1
                    student[n]-=1
            elif n==len(student)-1:
                if student[n-1] == 0:
                    student[n-1] += 1
                    student[n] -= 1
            else:
                if student[n-1] == 0:
                    student[n-1] += 1
                    student[n] -= 1
                elif student[n+1]==0:
                    student[n+1]+=1
                    student[n]-=1
            if student[n] == 2:
                student[n] -= 1
            
    return sum(student)