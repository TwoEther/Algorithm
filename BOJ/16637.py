'''
    괄호 추가하기
    exp) 1-2*3+4
    1) 1-(2*3)+4
    2) 1-2*(3+4)
'''
l = int(input())
exp = input()

def Calculate(exp):
    oper = '*/+-'
    stack = [exp[0]]

    while stack:
        for idx in range(1, len(exp)):
            if exp[idx] not in oper:
                stack.append()
            else:
                if exp[idx] == '+':
                    

    




