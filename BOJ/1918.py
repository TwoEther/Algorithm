exp = list(input())
s = ''
oper = [exp[1]]
s += exp[0]
priorty = {'*' : 1, '/' : 1, '+' : 0, '-' : 0, '(' : -1}            # 연산자 우선순위


def postFix(exp):  
    s = ''          # 연산결과를 저장할 문자열
    oper = []       # 연산자 스택

    for e in exp:
        # print(f's = {s} oper = {oper}')
        if len(oper) == 0 and e in '*/+-':      # 만일 연산자 배열이 비어있으면 삽입
            oper.append(e)
        else:
            if e in '(':                        # 왼쪽 괄호는 연산자 스택에 삽입
                oper.append(e)
            elif e in ')':                      # 오른쪽 괄호라면
                while True:
                    if len(oper) == 0:          # 배열이 비어있으면 중지
                        break
                    target = oper.pop()         # 연산자 배열에서 한개를 빼서
                    if target == '(':           # 만일 pop한 값이 오른쪽 괄호라면 중지
                        break
                    s += target                 # 문자열에 추가

            elif e in '*/':                     
                while True:
                    if len(oper) == 0:
                        break

                    target = priorty[oper[-1]]  # 연산자 배열 최상단 원소값을 가져옴
                    if target >= priorty[e]:    # 만일 연산자 순위가 크거나 같다면
                        s += oper.pop()         # pop시켜서 문자열에 추가
                    else:
                        break
                oper.append(e)
                        
            elif e in '+-':
                while True:
                    if len(oper) == 0:
                        break

                    target = priorty[oper[-1]]  # 위의 과정과 마찬가지
                    if target >= priorty[e]:
                        s += oper.pop()
                    else:
                        break
                oper.append(e)
            else:
                s += str(e)
    
    while oper:
        s += oper.pop()
    return s

print(postFix(exp))



