# 20
# Validating the Phone Number
# https://www.hackerrank.com/challenges/validating-the-phone-number/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

n = int(input())

for _ in range(n):
    print("YES" if re.fullmatch(r"[789]\d{9}", input()) else "NO")
