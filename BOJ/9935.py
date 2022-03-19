import sys
input = sys.stdin.readline

s = list(input().rstrip())
check = list(input().rstrip())
stack = []

for v in range(len(s)):
    stack.append(s[v])
    
    if len(stack) >= len(check):
        c = ''.join(stack[-len(check):])
        if c == ''.join(check):
            del stack[-len(check):]

result = ''.join(stack)

if result == '':
    print('FRULA')
else:
    print(result)
