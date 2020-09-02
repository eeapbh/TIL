def DFS(y, x):
    global result
    global count
    visited.append((y, x))

    if y == 0:
        result[x] = count
        return
    for d in range(3):
        ny = y+dy[d]
        nx = x+dx[d]
        if 0<=nx<100 and 0<=ny<100:
            if not (ny, nx) in visited and ladder[ny][nx] == 1:
                count += 1
                return DFS(ny, nx)

for _ in range(10):
    tc = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]

    start_y = 99
    start_x = 0
    dab = 0
    dy = [0, 0, -1]
    dx = [-1, 1, 0]
    result = {}
    for i in range(100):
        visited = []

        if ladder[99][i] == 1:
            count = 0
            start_x = i
            DFS(start_y, start_x)
    # print(result.keys())
    for k in result.keys():
        if result[k] == min(result.values()):
            dab = k

    print('#{} {}'.format(tc, dab))


