#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countApplesAndOranges' function below.
#
# The function accepts following parameters:
#  1. INTEGER s
#  2. INTEGER t
#  3. INTEGER a
#  4. INTEGER b
#  5. INTEGER_ARRAY apples
#  6. INTEGER_ARRAY oranges
#

def countApplesAndOranges(s, t, a, b, apples, oranges):
    outputs = [0,0]
    for apple in apples:
        a_d = apple + a
        if a_d >= s and a_d <= t:
            outputs[0]+=1
    for orange in oranges:
        o_d = orange + b
        if o_d >= s and o_d <= t:
            outputs[1]+=1
    print(outputs[0])
    print(outputs[1])
    
def countApplesAndOrangesSuperShort(s, t, a, b, apples, oranges):
    apple_sum = sum(1 for apple in apples if s <= apple+a <= t)
    orange_sum = sum(1 for orange in oranges if s <= orange + b <= t)
    print(apple_sum, orange_sum, sep='\n')

if __name__ == '__main__':


    s = 7

    t = 10



    a = 3

    b = 13

    apples = [5, 6, 2, 10, -1]

    oranges = [-10, -5, 20, -3, 1]  # example, -10 + 13 = 3.  3 is smaller than s , so its out of range

    countApplesAndOranges(s, t, a, b, apples, oranges)
