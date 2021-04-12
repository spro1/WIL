"""
    Date : 2021-04-11
    Source : https://www.hackerrank.com/challenges/divisible-sum-pairs/problem
"""
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the divisibleSumPairs function below.
def divisibleSumPairs(n, k, ar):
    cnt = 0
    for n, v in enumerate(ar):
        for v2 in ar[n+1:]:
            if (v+v2)%k == 0:
                cnt += 1
    return cnt
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
