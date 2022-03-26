import sys

test_case = int(input())

for t in range(test_case):
    files = [int(x) for x in input().split()]
    files.sort()
    result, length = files[0] * (len(files) - 1), len(files)
    
    for i in range(1, length):
        result += files[i] * (length-i)
    
    print(result)