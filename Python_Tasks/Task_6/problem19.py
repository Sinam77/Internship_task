# 19
# Company Logo
# https://www.hackerrank.com/challenges/most-commons/problem


#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter



if __name__ == '__main__':
    s = input()
    counts = Counter(sorted(s))
    for char, count in counts.most_common(3):
        print(char, count)
