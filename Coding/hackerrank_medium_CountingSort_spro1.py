"""
    Date : 2021-04-08
    Source : https://www.hackerrank.com/challenges/countingsort4/problem

"""
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countSort function below.
def countSort(arr):
    dic = {}
    n = len(arr)//2
    result = []
    for k, i in enumerate(arr):
        if k < n:
            i[1] = "-"
        if int(i[0]) in dic.keys():
            dic[int(i[0])].append(i[1])
        else:
            dic[int(i[0])] = []
            dic[int(i[0])].append(i[1])
    for i in sorted(dic):
        for l in dic[i]:
           result.append(l)
    print(" ".join(result))
    
if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(input().rstrip().split())

    countSort(arr)
