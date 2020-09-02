import sys
sys.stdin = open('input.txt', 'r')

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1] #상하좌우
def DFS(x, y):
    global count
    visited.append((x, y))
    count += 1
    for i in range(4):
        nx = x+dr[i]
        ny = y+dc[i]
        if 0<=nx<n and 0<=ny<n:
            if not (nx, ny) in visited and arr[nx][ny] == 1:
                DFS(nx, ny)


n = int(input())
arr = [list(map(int, input())) for _ in range(n)]
visited = []
save = []
count = 0
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1 and not (i, j) in visited:
            DFS(i, j)
            save.append(count)
            count = 0

print(len(save))
save.sort()
for i in save:
    print(i)