# 3
# Mars Exploration
# https://www.hackerrank.com/challenges/mars-exploration/problem
import math
import os
import random
import re
import sys

#
# Complete the 'marsExploration' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def marsExploration(s):
    # Write your code here
    
    expected = "SOS"
    return sum(1 for i, ch in enumerate(s) if ch != expected[i % 3])


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()
