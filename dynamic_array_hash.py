##DYNAMIC ARRAY
#Make a 2D dimensional array, with n amount of empty arrays inside of it. 
#Make sure you don't just input the same array multiple times, or you'll be pointing back to it. My note, this one.
#You are given an ARRAY named Queries with 3 types of values (so size of 3 columns per row):
#Type, X, Y
#Type is the type of query to be done. its int, either 1 or 2
#X will be used to calculate idx. its int, any
#Y will be used depending on the query. its int, any
#You also declare a variable called LastAnswer
# Query Type 1:
#   idx = (x ^ LastAnswer) % n # ^ is XOR operator
#   arr.append(idx)
# Query Type 2:
#   idx = (x ^ LastAnswer) % n
#   LastAnswer = arr[idx][y%len(arr[idx])]
#   answersArray.append(LastAnswer)
#
## CONSTRAINS
# n and q equal to or greater than 1
# n and q never larger than 10^5
# x and y equal to or greater than 0
# n and q never larger than 10^9
#
#Here follows the function I created, without the input.

import math
import os
import random
import re
import sys

def dynamicArray(n, queries):
    arr = []
    for _ in range(n):
        x = []
        arr.append(x)
    lastAnswer = 0
    answerArray = []
    for t,x,y in queries:
        result = (x^lastAnswer) % n
        if (t == 1):
            arr[result].append(y)
        elif (t == 2 ):
            lastAnswer = arr[result][y%len(arr[result])]
            answerArray.append(lastAnswer)
    return answerArray