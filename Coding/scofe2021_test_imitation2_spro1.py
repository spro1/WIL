# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
"""
    Date : 2021-03-19
    Source : scofe2021 모의테스트
"""
user_input = raw_input()
# N = 시즌 한정, M = 일반 음료
# 상품 1 =최소 5개의 시즌한정 + 쿠폰 7개 (총12개)
for i in range(0, int(user_input)):
   value_input = raw_input()
   value_input = value_input.split(" ")
   N = long(value_input[0])
   M = long(value_input[1])
   if(N < 5 or N+M < 12):   print(0)
   else:
      max_cnt = int((N+M)/12)
      can_cnt = int(N/5)
      result = max_cnt if max_cnt < can_cnt else can_cnt 
      while(N+M < 12*result):
         if(result==0): break
         result-=1;
      
      print(result)