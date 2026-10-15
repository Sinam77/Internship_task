# Problem 12: Introduction to Sets
# https://www.hackerrank.com/challenges/py-introduction-to-sets/problem

def average(array):
    unique = set(array)
    avg = sum(unique) / len(unique)
    return avg


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
