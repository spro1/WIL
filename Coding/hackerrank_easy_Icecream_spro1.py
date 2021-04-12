"""
    Date : 2021-04-09
    Source : https://www.hackerrank.com/challenges/icecream-parlor/problem
"""
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the icecreamParlor function below.
def icecreamParlor(m, arr):
    result = []
    for i in range(len(arr)):
        for l in range(i+1, len(arr)):
            if m == arr[i]+arr[l]:
                result = [i+1, l+1]
                return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        m = int(input())

        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = icecreamParlor(m, arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
