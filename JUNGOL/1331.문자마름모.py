dx = [1, 1, -1, -1, 0]
dy = [-1, 1, 1, -1, -1]

n = int(input())
m = n*2 -1
arr = [[0]*m for _ in range(m)]

x = 0
y = m//2
num = 1
arr[0][m//2] = 1
idx = 0
while 1:
    nx = x + dx[idx]
    ny = y + dy[idx]
    if 0 <= nx < m and 0 <= ny < m and arr[nx][ny] == 0:
        num += 1
        if num == 27:
            num = 1
        arr[nx][ny] = num
        x = nx
        y = ny
    else:
        x = nx - dx[idx]
        y = ny - dy[idx]
        if idx == 0 and arr[x+1][y] == 0:
            arr[x+1][y] = -1
        elif idx == 1 and arr[x][y+1] == 0:
            arr[x][y+1] = -1
        elif idx == 2 and arr[x-1][y] == 0:
            arr[x-1][y] = -1
        idx = (idx + 1) % 5
    if num == ((n-1)*n*4//2) + 1:
        break

for i in range(m):
    for j in range(m):
        if arr[i][j] > 0:
            print(chr(64 + arr[i][j]), end=' ')
        else:
            print(' ', end=' ')
    print()