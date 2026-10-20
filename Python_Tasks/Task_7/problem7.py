# 7
# Alphabet Rangoli
# https://www.hackerrank.com/challenges/alphabet-rangoli/problem
def print_rangoli(size):
    chars = [chr(97 + k) for k in range(size)]
    width = 4 * size - 3
    lines = []

    for i in range(size):
        left = chars[size - 1 - i:][::-1]
        full = left + left[-2::-1]
        lines.append('-'.join(full).center(width, '-'))

    print('\n'.join(lines + lines[-2::-1]))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
