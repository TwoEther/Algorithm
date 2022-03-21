import math
import sys
from collections import Counter

input = sys.stdin.readline

test_case = int(input())


for t in range(test_case):
    result = ''
    n = int(input())
    div = 2
    while n != 1:
        if n % div == 0 and div != n:
            n //= div
            result += str(div)
            continue
        div += 1

    for c in Counter(result).most_common():
        print(c[0], c[1])