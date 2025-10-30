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

# This method unfortunately is not efficient at all. It takes really long, and its a brute force method
# What needs to be applied, is a prefix sum solution

#A prefix sum is essentially an array that, for every indice a and indice b defined, you add the k value ONLY
# at a-1 and b positions of the array.
#This means, if i have an arr like so: [0,0,0,0,0]  (so n =5) , and these queries:
#(a=3, b=5, k=100)
#(a=1, b=4, k=100)
#(a=3, b=4, k=100)
# I would end up with this arr after the first run:
#[0,0,100,0,100,-100]     ## AS you can see, n+1 so I can mark the ending flag PAST the final digit.
#Then:
#[100,0,100,-100,100,-100]
#Finally:
#[100,0,200,-200,100,-100]
#This way I skip doing operations for every single variable
#Then I add everything onto a running variable:
# running+=100
# 
#And for every variable, I can check if it surpasses the biggest value I've seen
# if running > max_val
#max_val = running
    
        

    
            
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
