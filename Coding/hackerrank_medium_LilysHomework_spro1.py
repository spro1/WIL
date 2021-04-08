"""
    Date : 2021-04-08
    Source : https://www.hackerrank.com/challenges/lilys-homework/problem
    비고 : 파이썬은 call by assignment 함수로 배열을 보내면 ovject-reference 방식으로 mutable한 객체는 변경가능
"""

#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the lilysHomework function below.
def lilysHomework(arr):
    cnt = 0
    copy_arr = sorted(arr)
    print(arr)
    print(copy_arr)
    idx_arr = {}
    for n, v in enumerate(arr):
        idx_arr[v] = n

    for i in range(len(arr)):
        if arr[i] != copy_arr[i]:
            cnt += 1
            change_idx = idx_arr[copy_arr[i]]
            idx_arr[arr[i]] = change_idx
            arr[i], arr[change_idx] = arr[change_idx], arr[i]
    return cnt


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))
    reverse_arr = arr[::-1]
    asc, dsc = lilysHomework(arr), lilysHomework(reverse_arr)

    print(asc, dsc)
    result = min(asc, dsc)

    fptr.write(str(result) + '\n')

    fptr.close()
