# 15
# Game of Thrones - I
# https://www.hackerrank.com/challenges/game-of-thrones/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gameOfThrones' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#
from collections import Counter
def gameOfThrones(s):
    # Write your code here
    odd = sum(1 for c in Counter(s).values() if c % 2 == 1)
    return "YES" if odd <= 1 else "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = gameOfThrones(s)

    fptr.write(result + '\n')

    fptr.close()
