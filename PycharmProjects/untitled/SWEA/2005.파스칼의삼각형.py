t = int(input())
for tc in range(1, t+1):
    n = int(input())

    arr = [[0]*n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            arr[0][0] = 1
            if 0<= x-1 < n and 0<= y-1 <n:
                L = arr[x - 1][y - 1]
                R = arr[x - 1][y]
                arr[x][y] = L + R
            else:
                R = arr[x - 1][y]
                arr[x][y] = R
    print(f'#{tc}')
    for i in range(n):

        for j in range(n):
            if arr[i][j] != 0:
                print(arr[i][j], end = ' ')
        print()