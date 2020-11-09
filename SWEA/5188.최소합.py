import sys
sys.stdin = open('input.txt', 'r')
from collections import deque

delta = [(1, 0), (0, 1)]
def bfs(x, y):
    q = deque()
    q.append((x, y))
    while q:
        cx, cy = q.popleft()
        for i in range(2):
            nx = cx+delta[i][0]
            ny = cy+delta[i][1]
            if 0<=nx<n and 0<=ny<n:
                if dist[nx][ny] > dist[cx][cy] + arr[nx][ny]:
                    dist[nx][ny] = dist[cx][cy] + arr[nx][ny]
                q.append((nx, ny))
t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    dist = [[10*n]*n for _ in range(n)]
    dist[0][0] = arr[0][0]
    bfs(0, 0)
    print('#{} {}'.format(tc, dist[n-1][n-1]))

