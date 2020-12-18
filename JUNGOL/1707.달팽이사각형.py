n = int(input())

arr = [[0]*n for _ in range(n)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
arr[0][0] = 1
num = 1
x = y = 0
idx = 0
while 1:
    if num == n*n:
        break
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
        idx = (idx+1) % 4
for i in range(n):
    for j in range(n):
        print(arr[i][j], end=' ')
    print()