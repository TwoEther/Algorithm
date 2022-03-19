import sys

while True:
    result = 'yes'
    stack = []  # () 괄호를 1 [] 를 2로 표현
    string = sys.stdin.readline().rstrip()
    if string == '.':
        break
    
    for s in string:
        if s == '(':
            stack.append(1)
        elif s == '[':
            stack.append(2)
        elif s == ')':
            if len(stack) == 0 or stack[-1] != 1:
                result = 'no'
                break
            else:
                stack.pop()    
        elif s == ']':
            if len(stack) == 0 or stack[-1] != 2:
                result = 'no'
                break
            else:
                stack.pop()

    if len(stack) != 0:
        print('no')
    else: 
        print(result)