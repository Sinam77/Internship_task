# 18
# Set Mutations
# https://www.hackerrank.com/challenges/py-set-mutations/problem
# Enter your code here. Read input from STDIN. Print output to 
input()  # size of A, not needed
a = set(map(int, input().split()))
n = int(input())

for _ in range(n):
    command, _size = input().split()
    other = set(map(int, input().split()))
    getattr(a, command)(other)

print(sum(a))
