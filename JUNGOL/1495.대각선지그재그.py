n = int(input())
arr = [[0]*n for _ in range(n)]
dx = [1, -1]
dy = [-1, 1]
x = 0
y = 0
idx = 0
num = 1
c1 = 0
c2 = 0
cnt = 0
arr[0][0] = 1
while 1:

    nx = x + dx[idx]
    ny = y + dy[idx]
    if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == 0:
        num += 1
        arr[nx][ny] = num
        x = nx
        y = ny
    else:

        x = nx - dx[idx]
        y = ny - dy[idx]
        if c1 < n-1:
            c1 += 1
            if idx == 0:
                x = c1
                y = 0
            else:
                x = 0
                y = c1
            num += 1
            arr[x][y] = num
        else:
            c2 += 1
            if idx == 0:
                x = n - 1
                y = c2
            else:
                x = c2
                y = n - 1
            num += 1
            arr[x][y] = num
        idx = (idx+1)%2
    if num == n*n:
        break
for i in range(n):
    for j in range(n):
        print(arr[i][j], end=' ')
    print()





