"""
    Date : 2021-04-08
    Source : https://www.hackerrank.com/challenges/lilys-homework/problem
    비고 : median을 구할 때 sort를 사용하면 시간복잡도가 증가하므로 counting sort를 구현하여 median 값을 구해준다.
"""

#!/bin/python3

import math
import os
import random
import re
import sys


def get_median(data, d):
    median, count = 0, 0
    if d % 2 == 1:
        for i in range(len(data)):
            count += data[i]
            if count > d // 2:
                median = i
                break
    else:
        m1, m2 = 0, 0
        for i in range(len(data)):
            count += data[i]
            if m1 == 0 and count >= d // 2:
                m1 = i
            if m2 == 0 and count >= d // 2 + 1:
                m2 = i
                break
        median = (m1 + m2) / 2
    return median


# Complete the activityNotifications function below.
def activityNotifications(expenditure, d):
    notice = 0

    countArr = [0 for _ in range(201)]
    for i in range(d):
        countArr[expenditure[i]] += 1

    for i in range(d, len(expenditure)):
        median = get_median(countArr, d)
        if expenditure[i] >= median * 2:
            notice += 1

        countArr[expenditure[i]] += 1
        countArr[expenditure[i - d]] -= 1

    return notice


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()
