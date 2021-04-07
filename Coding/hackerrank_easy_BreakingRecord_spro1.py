"""
    Date : 2021-04-07
    Source : https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem

"""
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    max_s = scores[0]
    min_s = scores[0]
    max_c = 0
    min_c = 0
    for n, v in enumerate(scores[1:]):
        if v > max_s:
            max_s = v
            max_c += 1
        elif v < min_s:
            min_s = v
            min_c += 1
    return [max_c, min_c]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
