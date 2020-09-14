import sys
sys.stdin = open('input.txt', 'r')
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def DFS(x, y):
    visit.append((x, y))
    arr[x][y] = 0
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<n and 0<=ny<n:
            if arr[nx][ny] == 1 and (nx, ny) not in visit:
                DFS(nx, ny)



n = int(input())
arr = [list(map(int, input())) for _ in range(n)]

result = []
for i in range(n):
    for j in range(n):
        visit = []
        if arr[i][j] == 1:
            DFS(i, j)
            result.append(len(visit))
print(len(result))
result.sort()
for r in result:
    print(r)
