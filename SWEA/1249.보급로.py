import sys
sys.stdin = open('input.txt', 'r')

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    q = []
    q.append((x, y))
    while q:
        cx, cy = q.pop(0)
        for i in range(4):
            nx = cx+dx[i]
            ny = cy+dy[i]
            if 0<=nx<n and 0<=ny<n:
                if dist[nx][ny] > dist[cx][cy] + arr[nx][ny]:
                    dist[nx][ny] = dist[cx][cy] + arr[nx][ny]
                    q.append((nx, ny))


t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input())) for _ in range(n)]
    dist = [[987654321]*n for _ in range(n)]
    dist[0][0] = 0
    bfs(0, 0)
    print('#{} {}'.format(tc, dist[n-1][n-1]))