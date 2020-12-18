dx = [1, 0, -1]
dy = [1, -1, 0]
n = int(input())
num = 0
cnt = 0
arr = [[-1]*n for _ in range(n)]
x = y = 0
idx = 0
arr[x][y] = 0
while 1:


    nx = x + dx[idx]
    ny = y + dy[idx]
    if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] < 0:
        num += 1
        cnt += 1
        if num == 10:
            num = 0
        arr[nx][ny] = num
        x = nx
        y = ny
    else:
        x = nx - dx[idx]
        y = ny - dy[idx]
        idx += 1
        idx = idx % 3
    if cnt == (n*(n+1)//2) - 1:
        break

for i in range(n):
    for j in range(n):
        if arr[i][j] >= 0:
            print(arr[i][j], end=' ')
    print()

