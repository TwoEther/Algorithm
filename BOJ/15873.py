exp = input()

if len(exp) == 2:
    result = int(exp[0]) + int(exp[1])
elif len(exp) == 3:
    idx = exp.find('0')
    if idx == 1:
        idx2 = 2
    else:
        idx2 = 0
    result = int(exp[idx-1:idx+1]) + int(exp[idx2])
else:
    result = 20
print(result)