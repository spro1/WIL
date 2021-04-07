"""
    Date : 2021-04-07
    Source : https://www.hackerrank.com/challenges/a-very-big-sum/problem
    비고 : 파이썬은 long 타입이 따로 없이 int형을 사용해도 오버플로우가 일어나지 않으므로
    별다른 수정 사항이 없다.

"""
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the aVeryBigSum function below.
def aVeryBigSum(ar):
    result = 0
    for x in ar:
        result += x
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = aVeryBigSum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
