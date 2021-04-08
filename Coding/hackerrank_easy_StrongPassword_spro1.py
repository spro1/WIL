"""
    Date : 2021-04-08
    Source : https://www.hackerrank.com/challenges/strong-password/problem

"""
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumNumber function below.
def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    x = 0
    if not re.search('[0-9]+', password):
        x+=1
    if not re.search('[a-z]+', password):
        x+=1
    if not re.search('[A-Z]+', password):
        x+=1
    if not re.search('[\!\@\#\$\%\^\&\*\(\)\-\+]', password):
        x+=1
    print('x:',x)
    if len(password) < 6:
        if 6-len(password) <= x:
            return x
        else:
            return 6-len(password)
    return x
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
