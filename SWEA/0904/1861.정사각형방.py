import sys
sys.stdin = open('input.txt', 'r')
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def BFS(x, y):
    global cnt
    cnt += 1
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<n and 0<=ny<n and arr[nx][ny]- arr[x][y] == 1:
            BFS(nx, ny)
        else:
            save.append((cnt, arr[x][y]))


t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    save = []
    for i in range(n):
        for j in range(n):
            cnt = 0
            BFS(i, j)
    result = 0
    save.sort(key=lambda x:(-x[0], x[1]))
    print(save)

