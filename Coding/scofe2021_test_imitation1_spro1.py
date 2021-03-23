# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
"""
    Date : 2021-03-19
    Source : scofe2021 모의테스트
"""
user_input = input()
user_input=user_input.split(" ")
n = int(user_input[0])
k = int(user_input[1])
cnt = 1
while(n > k):
   n -= k
   if(n!=1):
      n+=1
   cnt+=1
print(cnt)