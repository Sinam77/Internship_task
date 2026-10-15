# Problem 19: Collections.Counter()
# https://www.hackerrank.com/challenges/collections-counter/problem

from collections import Counter

x = int(input())

sizes = list(map(int, input().split()))

stock = Counter(sizes)

n = int(input())

total = 0

for i in range(n):
    size, price = map(int, input().split())

    if stock[size] > 0:
        total += price
        stock[size] -= 1

print(total)
