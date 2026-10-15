# Problem 15: Word Order
# https://www.hackerrank.com/challenges/word-order/problem

n = int(input())

freq = {}

for i in range(n):
    word = input()

    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

print(len(freq))
print(*freq.values())
