import sys
input = sys.stdin.readline

n = int(input())
exp = input().rstrip()
alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
my_dict = {}
stack = []
s = ''

for i in range(n):
    my_dict[alpha[i]] = int(input())

for e in exp:
    if e not in '*/+-':
        stack.append(e)
    else:
        v2, v1 = stack.pop(), stack.pop()
        
        if str(v1) in alpha:
            v1 = int(my_dict[v1])

        if str(v2) in alpha:
            v2 = int(my_dict[v2])
        if e == '+':
            stack.append(v1+v2)
        elif e == '-':
            stack.append(v1-v2) 
        elif e == '*':
            stack.append(v1*v2)
        else:
            stack.append(v1/v2)
        # print(f'v1 = {v1} v2 = {v2}')
    # print(f'stack = {stack}')
result = stack[0]
print('{:.2f}'.format(result))
