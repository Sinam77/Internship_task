# 16
# Check Subset
# https://www.hackerrank.com/challenges/py-check-subset/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT
t = int(input())

for _ in range(t):
    input()  # size of A, not needed
    a = set(input().split())
    input()  # size of B, not needed
    b = set(input().split())
    print(a.issubset(b))
