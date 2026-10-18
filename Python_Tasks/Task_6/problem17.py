# 17
# Check Strict Superset
# https://www.hackerrank.com/challenges/py-check-strict-superset/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT
a = set(input().split())
n = int(input())

print(all(a > set(input().split()) for _ in range(n)))
