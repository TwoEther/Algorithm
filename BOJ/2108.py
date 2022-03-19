from collections import Counter
import sys

input = sys.stdin.readline
t = int(input())
numbers = []
radix = [-4002 for x in range(8001)]
for idx in range(t):
    n = int(input())
    numbers.append(n)
numbers.sort()

# 산술평균
print('-------------')
print(f'{round(sum(numbers)/t)}')

# 중앙값

print(f'{numbers[t//2]}')

# 최빈값
if t == 1:
    print(numbers[-1])
else:
    for idx in range(len(numbers)):
        radix[numbers[idx]+4000] += 1
        # print(f'radix[{numbers[idx]+4000}] =  {radix[numbers[idx]+4000]}')
    
    second = -4001
    max_value = max(radix)
    for i in range(len(radix)):
        if second <= radix[i]:
            second = radix[i]
        
    if second == max_value:
        print(max_value+4000)
    else:
        print(second+4000)
# 범위
print(f'{max(numbers)-min(numbers)}')

