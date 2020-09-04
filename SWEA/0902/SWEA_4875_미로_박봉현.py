import sys
sys.stdin = open('input.txt', 'r')

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def DFS(x, y):
    global result
    visited.append((x, y))

    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<n and 0<=ny<n:
            if not (nx, ny) in visited and arr[nx][ny] != 1:
                if arr[nx][ny] == 3:
                    result = 1
                DFS(nx, ny)

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input())) for _ in range(n)]
    visited = []
    result = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 2:
                DFS(i, j)
                break
    print('#{} {}'.format(tc, result))