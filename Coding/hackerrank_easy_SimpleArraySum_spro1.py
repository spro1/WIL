"""
    Date : 2021-04-07
    Source : https://www.hackerrank.com/challenges/simple-array-sum/problem

"""

#!/bin/python3

import os
import sys

#
# Complete the simpleArraySum function below.
#
def simpleArraySum(ar):
    #
    # Write your code here.
    #
    result = 0
    for x in ar:
        result += x
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    ar_count = int(input())
    ar = list(map(int, input().rstrip().split()))
    result = simpleArraySum(ar)
    fptr.write(str(result) + '\n')
    fptr.close()
