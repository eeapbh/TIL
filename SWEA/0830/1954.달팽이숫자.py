
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = [[0]*n for _ in range(n)]
    # 우 하 좌 상 돔
    # 벽을만나거나 0이아닌곳을 만나면 방향바꿈
    x = y = d =0
    cnt = 1
    while cnt <= n*n:
        arr[x][y] = cnt
        cnt += 1

        nx = x+dx[d]
        ny = y+dy[d]

        if 0<=nx<n and 0<=ny<n and arr[nx][ny] == 0:
            x = nx
            y = ny
        else:
            d = (d+1)%4
            x += dx[d]
            y += dy[d]

    print('#{}'.format(tc))
    for i in range(n):
        for j in range(n):
            print(arr[i][j], end=' ')
        print()