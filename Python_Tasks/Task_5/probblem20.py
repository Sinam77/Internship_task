# 20
# Piling Up!
# https://www.hackerrank.com/challenges/piling-up/problem

#Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque

t = int(input())

for i in range(t):
    n = int(input())
    cubes = deque(map(int, input().split()))

    previous = float('inf')
    possible = True

    while cubes:
        if cubes[0] >= cubes[-1]:
            current = cubes.popleft()
        else:
            current = cubes.pop()

        if current > previous:
            possible = False
            break

        previous = current

    print("Yes" if possible else "No")
