sto = [[int(x) for x in input().split()] for y in range(9)]
e = 0
pos = []

for y in range(9):
    for x in range(9):
        if sto[y][x] == 0:
            e += 1
            pos.append((x,y))

def checkPos(x, y, stock, v):
    stock[y][x] = v
    target = stock[y][x]

    # 세로줄 검사
    for posY in range(0, 9):
        if posY == y:
            continue
        if stock[posY][x] == target:
            return False
    
    # 가로줄 검사
    for posX in range(0, 9):
        if posX == x:
            continue
        if stock[y][posX] == target:
            return False

    # 영역검사
    startX = (int(x//3))*3
    startY = (int(y//3))*3

    for posY in range(startY, startY+3):
        for posX in range(startX, startX+3):
            if posX == x and posY == y:
                continue
            if stock[posY][posX] == target:
                return False
    return True


def BT(stock, empty, depth, empty_pos):
    if depth == empty:
        return stock
    else:
        for v in range(1, 10):
            x, y = empty_pos[depth]
            if not checkPos(x, y, stock, v):                       # 적합하지 않으면 V의값 수정
                continue
            else:
                stock[y][x] = v
                return BT(stock, empty, depth+1, empty_pos)     # 적합하면 다음 좌표로 이동

result = BT(sto, e, 0, pos)

for y in range(9):
    for x in range(9):
        print(result[y][x], end=' ')
    print()


