def dfs(y, x):
    visited[y][x] = 1
    global result

    if y == 0:
        result = x
        return

    for i in range(3):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < 100 and 0 <= ny < 100:
            if not visited[ny][nx] and arr[ny][nx] == 1:
                return dfs(ny, nx)

for tc in range(1, 11):
    tcn = input()
    arr = [list(map(int, input().split())) for _ in range(100)]
    visited = [[0] * 100 for _ in range(100)]
    dx = [1, -1, 0]
    dy = [0, 0, -1]
    result = 0
    y, x = 99, arr[99].index(2)
    dfs(y, x)
    print('#{} {}'.format(tc, result))
