'''
    투포인터 알고리즘
    1. start와 end를 맨 처음에 위치시킨다
    2. end를 증가시키면서 start와 end사이의 원소합을 구한다
    3. 만일 구간합이 값보다 작다면 end를 증가하고 크다면 start를 증가한다
    4. 같으면 카운트하고 end를 증가시킨다
    5. start와 end가 마지막원소를 접근한후 종료한다
'''
import sys

input = sys.stdin.readline
n = int(input())
nums = [int(x) for x in input().split()]
k = int(input())
result = 0

start, end = 0, 0

while end < len(nums):
    s_sum = sum(nums[start], nums[end])
    print(s_sum)
    if s_sum == k:
        result += 1
    elif s_sum < k:
        end += 1
    else:
        start += 1

print(result)