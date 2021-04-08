"""
    Date : 2021-04-07
    Source : https://www.hackerrank.com/challenges/time-conversion/problem

"""
#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    #
    # Write your code here.
    #
    if s[-2:]=="PM":
        s = s[:-2].split(":")
        s[0] = "12" if str(int(s[0])+12)=="24" else str(int(s[0])+12)
    else:
        s = s[:-2].split(":")
        if s[0] == "12":
            s[0] = "00"
    return ":".join(s)
if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
