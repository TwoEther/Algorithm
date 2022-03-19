import sys

input = sys.stdin.readline
n = int(input())
a = [int(x) for x in input().split()]
numbers = [int(x) for x in input().split()]

def bt(depth, nums, max_value, min_value, current):
    if depth == sum(numbers):
        return min_value, max_value
    else:
        for i in range(len(nums)):
            if nums[i] == 0:
                continue

            if i == 0:
                current += nums[depth+1]
            elif i == 1:
                current -= numbers[depth+1]
            elif i == 2:
                current *= numbers[depth+1]
            else:
                current //= numbers[depth+1]
                