import sys
sys.stdin = open('input.txt', 'r')

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def check(x, y):
    global cnt

    v = arr[x][y]
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<n and 0<=ny<n:
            if abs(arr[nx][ny]-v) == 1:
                check(nx, ny)
                cnt += 1
    return cnt

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    result = {}
    for i in range(n):
        for j in range(n):
            cnt = 1
            result[arr[i][j]] = check(i, j)

    for k, v in result.items():
        if v == max(result.values()):
            print('#{} {} {}'.format(tc, k, v))