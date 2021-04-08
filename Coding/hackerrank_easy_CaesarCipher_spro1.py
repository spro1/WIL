"""
    Date : 2021-04-08
    Source : https://www.hackerrank.com/challenges/caesar-cipher-1/problem

"""
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the caesarCipher function below.
def caesarCipher(s, k):
    result = ''
    for i in s:
        i = ord(i)
        if(65<= i <=90) or (97<=i<=122):
            if (65<=i<=90):
                while i+k > 90:
                    i-=26
            elif (97<=i<=122):
                while i+k > 122:
                    i-=26
            result += chr(i+k)
        else:
            result += chr(i)
    return result
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    k = int(input())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
