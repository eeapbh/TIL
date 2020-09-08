import sys
sys.stdin = open('input.txt', 'r')
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def DFS(x, y):
    global cnt

    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<n and 0<=ny<n and arr[nx][ny]- arr[x][y] == 1:
            cnt += 1
            DFS(nx, ny)
    return cnt


t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    save = []
    for i in range(n):
        for j in range(n):
            cnt = 1
            save.append((arr[i][j], DFS(i, j)))

    save.sort(key=lambda x:(-x[1],x[0]))

    print('#{} {} {}'.format(tc, save[0][0], save[0][1]))
