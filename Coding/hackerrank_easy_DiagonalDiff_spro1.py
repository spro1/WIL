"""
    Date : 2021-04-07
    Source : https://www.hackerrank.com/challenges/diagonal-difference/problem

"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    left = 0
    right = 0
    for k, v in enumerate(arr):
        for kk, vv in enumerate(arr):
            if k==kk:
                left += v[k]
    for k, v in enumerate(arr[::-1]):
        for kk, vv in enumerate(arr[::-1]):
            if k==kk:
                right += v[k]
    if right>=left:
        return right-left
    else:
        return left-right
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
