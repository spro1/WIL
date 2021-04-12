"""
    Date : 2021-04-09
    Source : https://www.hackerrank.com/challenges/sum-vs-xor/problem

"""
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sumXor function below.
def sumXor(n):
    c = 0
    while(n):
        if n%2==0:
            c+=1
        n//=2
    return 2**c
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = sumXor(n)

    fptr.write(str(result) + '\n')

    fptr.close()
