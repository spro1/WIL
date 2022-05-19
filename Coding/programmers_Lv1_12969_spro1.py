"""
    Date: 2022-05-19
    Source: https://programmers.co.kr/learn/courses/30/lessons/12969
"""
a, b = map(int, input().strip().split(' '))
s = ""
for i in range(b):
    for l in range(a):
        s+="*"
    s+="\n"
print(s)

"""
a, b = map(int, input().strip().split(' '))
answer = ('*'*a +'\n')*b
print(answer)
"""