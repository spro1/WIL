"""
    Date : 2021-04-09
    Source : https://www.hackerrank.com/challenges/sherlock-and-array/problem
"""
#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the balancedSums function below.
def balancedSums(arr):
    front_sum = 0
    back_sum = sum(arr)
    for i in range(len(arr)):
        back_sum-=arr[i]
        if front_sum == back_sum:
            return "YES"
        elif front_sum > back_sum:
            return "NO"
        else:
            front_sum += arr[i]
    return "NO"
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = balancedSums(arr)

        fptr.write(result + '\n')

    fptr.close()
