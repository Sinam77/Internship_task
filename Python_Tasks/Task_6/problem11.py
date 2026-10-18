# 11
# String Formatting
# https://www.hackerrank.com/challenges/python-string-formatting/problem

def print_formatted(n):
    # your code goes here
   
    width = len(bin(n)) - 2  # strip the '0b' prefix
    for i in range(1, n + 1):
        print(f"{i:{width}d} {i:{width}o} {i:{width}X} {i:{width}b}")


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
