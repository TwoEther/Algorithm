from ast import Index
import sys

input = sys.stdin.readline

n = int(input())
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
result = 0

sorted_a = sorted(a, reverse=True)
sorted_b = sorted(b)

for i in range(len(a)):
    result += sorted_a[i] * sorted_b[i]
    
print(result)

