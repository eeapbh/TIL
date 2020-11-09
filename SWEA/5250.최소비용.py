

import sys
sys.stdin = open('input.txt', 'r')

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    q = []
    q.append((x, y))
    visit.append((x, y))
    while q:
        cx, cy = q.pop(0)
        for i in range(4):
            nx = cx+dx[i]
            ny = cy+dy[i]
            if 0<=nx<n and 0<=ny<n and not (nx, ny) in visit:
                q.append((nx, ny))
                visit.append((nx, ny))
                if dist[nx][ny] > dist[cx][cy] - arr[cx][cy]+1:
                    dist[nx][ny] = dist[cx][cy] - arr[cx][cy]+1

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    dist = [[99999]*n for _ in range(n)]
    visit = []
    dist[0][0] = 0
    bfs(0, 0)
    print(dist)
    print(dist[n-1][n-1])