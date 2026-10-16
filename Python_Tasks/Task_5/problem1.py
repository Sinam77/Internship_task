# 1
# Find the Runner-Up Score!
# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem


if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    unique_arr = set(arr)
    sorted_arr = sorted(unique_arr, reverse=True)
    print(sorted_arr[1])
