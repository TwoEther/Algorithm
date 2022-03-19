import sys

input = sys.stdin.readline
numbers = []
operation = []

stackNumber, curentIdx = 1, 0
n = int(input())

for i in range(n):
    numbers.append(int(input()))

stack = []

while True:
    oper = '+'
    if stackNumber > n:                         # 스택에 전부 삽입하였다면
        if len(stack) == 0:                     # 이때 스택이 비었으면 중지
                for o in operation:
                    print(o)
                break
        if stack[-1] != numbers[curentIdx]:     # 스택의 최상단이 비교값과 같지 않다면 중지
            print('NO')
            break
        else:
            stack.pop()                         
            oper = '-'
            curentIdx += 1
    else:
        if len(stack) == 0:
            stack.append(stackNumber)
            stackNumber += 1
        else:
            if stack[-1] == numbers[curentIdx]:
                stack.pop()
                curentIdx += 1
                oper = '-'
            else:
                stack.append(stackNumber)
                stackNumber += 1
    operation.append(oper)


