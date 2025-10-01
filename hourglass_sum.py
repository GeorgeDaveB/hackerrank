#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#
    
    
def hourglassSum(arr):
    start = 1
    end = len(arr) - 1
    max_sum = float("-inf")
    for i in range (start, end):
        for j in range (start, end):
            now_sum = 0
            for z in range (-1, 2):
                now_sum = now_sum + arr[i-1][j+z] + arr[i+1][j+z]
            now_sum = now_sum + arr[i][j] #add the center of the hourglass
            if now_sum > max_sum:
                max_sum = now_sum
    return max_sum
            # print (f"number:{arr[i][j]} \ncurrent index: {i}, {j}")
            # print (f"length of a line is {len(arr)}")
            
    
    # for i in range(len(arr) - 2):
    #     for j in range (len(arr) - 2):

        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()