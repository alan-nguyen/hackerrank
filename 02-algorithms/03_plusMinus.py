#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    count_neg = 0
    count_ze = 0
    count_pos = 0
    for i in arr:
        if i < 0:
            count_neg += 1
        elif i == 0:
            count_ze += 1
        else:
            count_pos += 1
    print(count_pos / n)
    print(count_neg / n)
    print(count_ze / n)

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
