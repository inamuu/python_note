#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#


def miniMaxSum(arr):
    sort_list = sorted(arr)
    sort_r_list = sorted(arr, reverse=True)
    mini = sum(sort_list[0:4])
    max = sum(sort_r_list[0:4])
    print(mini, max)


if __name__ == '__main__':

    #arr = list(map(int, input().rstrip().split()))
    arr = [10, 11, 12, 13, 14]

    miniMaxSum(arr)
