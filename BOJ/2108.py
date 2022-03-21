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
# print('-------------')
print(f'{round(sum(numbers)/t)}')

# 중앙값

print(f'{numbers[t//2]}')

# 최빈값
if t == 1:
    print(numbers[-1])
else:
    add_value = min(numbers)
    for i in range(len(numbers)):
        numbers[i] -= add_value - 1
    
    max_number = max(numbers)
    my_list = [0 for x in range(max_number)]
    
    for i in numbers:
        my_list[i-1] += 1
            
    max_value = max(my_list)      # 비교를 위한 변수
    num = 0
    for i in range(len(my_list)):
        if my_list[i] == max_value:     # 최빈값이 있다면
            num += 1                    # 최빈값 카운트
        
        if num == 2:                    # 만일 최빈값이 2개라면
            print(i + add_value)        # 출력
            break
    else:
        print(my_list.index(max(my_list))+ add_value)
    
# 범위
print(f'{max(numbers)-min(numbers)}')

