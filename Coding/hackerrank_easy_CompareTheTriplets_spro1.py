"""
    Date : 2021-04-07
    Source : https://www.hackerrank.com/challenges/compare-the-triplets/problem

"""
# !/bin/python3

import math
import os
import random
import re
import sys


# Complete the compareTriplets function below.
def compareTriplets(a, b):
    point_a = 0
    point_b = 0
    for n in range(len(a)):
        if a[n] > b[n]:
            point_a += 1
        elif b[n] > a[n]:
            point_b += 1
    return str(point_a) + str(point_b)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

