"""
    Date : 2021-04-07
    Source : https://www.hackerrank.com/challenges/reduced-string/problem

"""
#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the superReducedString function below.
def superReducedString(s):
    n = 0
    while 1:
        print(n, s)
        if n == len(s) - 1:
            return s
        if len(s) == 0:
            return "Empty String"
        if s[n] == s[n + 1]:
            s = s[:n] + s[n + 2:]
            print(s)
            n = 0
        else:
            n += 1
    return s

    return ''


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()
