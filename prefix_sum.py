#!/bin/python3

import math
import os
import random
import re
import sys
from pathlib import Path
import time

#
# Complete the 'arrayManipulation' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

        
def arrayManipulation(n, queries):
    spinner = ['|', '/', '-', '\\']
    arr = [0] * n
    # arr = []
    # for i in range(0, n):
    #     arr.append(0) #make an array of zeroes based on n
    #     print(i , " iterations")
    for query in queries:
        a = query[0]
        b = query[1]
        k = query[2]
        # print(a, b ,k)
        for i in range(a-1,b):
            # print(i)
            arr[i] = arr[i] + k
            sys.stdout.write(f"\rProcessing... {spinner[i % len(spinner)]}")
            sys.stdout.flush()
            time.sleep(0.1)  # simulate work
            arr.sort(reverse=True)
    for i in range (0, 100):
        print (arr[i])
    return arr[0]
    
        

    
            
if __name__ == '__main__':
    """Read first line as n, m; then read m lines of a,b,k."""
    file_path = r"D:\Dropbox\PROJECTS\hackerrank_scripts\testcase_12_array_add_k_to_indices.txt"
    queries = []
    with open(file_path, "r", encoding="utf-8") as f:
        # First line: n m
        first = f.readline()
        while first.strip() == "":        # skip any leading blank lines
            first = f.readline()
        n_str, m_str = first.split()
        n, m = int(n_str), int(m_str)

        # Next m lines: a b k
        for _ in range(m):
            line = f.readline()
            while line and line.strip() == "":  # skip occasional blank lines
                line = f.readline()
            a, b, k = map(int, line.split())
            queries.append((a, b, k))
    max_output = arrayManipulation(n, queries)
    print (max_output)
