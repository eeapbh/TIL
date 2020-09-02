def DFS(y, x):
    global result
    visited.append((y, x))
    if y == 0:
        result = x
        return
    for d in range(3):
        ny = y+dy[d]
        nx = x+dx[d]
        if 0<=nx<100 and 0<=ny<100:
            if not (ny, nx) in visited and ladder[ny][nx] == 1:
                return DFS(ny, nx)

for _ in range(10):
    tc = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]

    start_y = 99
    start_x = ladder[99].index(2)

    dy = [0, 0, -1]
    dx = [-1, 1, 0]
    result = 0
    visited = []
    DFS(start_y, start_x)
    print('#{} {}'.format(tc, result))