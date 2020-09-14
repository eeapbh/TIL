import sys
sys.stdin = open('input.txt', 'r')

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def BFS(x, y, c):
    q = []
    q.append((x, y, c))
    while q:

        currx, curry, currc = q.pop(0)
        visit.append((currx, curry))
        if currx == n-1 and curry == m-1:
            return currc

        for i in range(4):
            nx = currx+dx[i]
            ny = curry+dy[i]
            if 0<=nx<n and 0<=ny<m and arr[nx][ny] == 1 and (nx, ny) not in visit:
                q.append((nx, ny, currc+1))

n, m = map(int, input().split())
arr = [list(map(int, input())) for _ in range(n)]
visit = []
cnt = 1
tmp = []
print(BFS(0, 0, cnt))
