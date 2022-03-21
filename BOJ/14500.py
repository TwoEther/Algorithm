def findMaxValue(n, m, arr):
    maxValue = 0
    # -
    for y in range(n):
        for x in range(m-3):
            k = sum(arr[y][x:x+3])
            if maxValue <= k:
                maxValue = k
                
    # ㅁ
    for y in range(n-1):
        for x in range(m-1):
            k = sum(arr[y][x:x+2], sum)

