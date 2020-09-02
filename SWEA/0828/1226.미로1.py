import sys
sys.stdin = open('input.txt', 'r')

#상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def DFS(x, y):
    global result
    visited.append((x, y))
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<16 and 0<=ny<16:
            if not (nx, ny) in visited and arr[nx][ny] != 1:
                if arr[nx][ny] == 3:
                    result = 1
                DFS(nx, ny)

for _ in range(10):
    start_x = 0
    start_y = 0
    tc = int(input())
    arr = [list(map(int, input())) for _ in range(16)]
    for i in range(16):
        for j in range(16):
            if arr[i][j] == 2:
                start_x = i
                start_y = j
                break
    visited = []
    result = 0
    DFS(start_x, start_y)
    print(DFS(start_x, start_y))
    print('#{} {}'.format(tc, result))
