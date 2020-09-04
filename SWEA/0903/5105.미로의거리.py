import sys
sys.stdin = open('input.txt', 'r')

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def BFS(x, y):
    global total
    visited[x][y] = 1
    queue = []
    queue.append((x, y))
    while len(queue) > 0:
        cx, cy = queue.pop(0)
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0<= nx <n and 0<= ny < n:
                if visited[nx][ny] == 0 and arr[nx][ny] != 1:
                    queue.append((nx, ny))
                    visited[nx][ny] = visited[cx][cy] + 1

                    if arr[nx][ny] == 3:
                        total = visited[nx][ny]-2
                        return

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input())) for _ in range(n)]
    visited = [[0]*n for _ in range(n)]
    total = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 2:
                BFS(i, j)
    print('#{} {}'.format(tc, total))


