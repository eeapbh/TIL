import sys
sys.stdin = open('input.txt', 'r')

sys.setrecursionlimit(10000)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
# 왜런타임에러뜨지
# def DFS(x, y):
#     q = []
#     q.append((x, y))
#     while q:
#         currx, curry = q.pop(0)
#         arr[currx][curry] = 0
#         for i in range(4):
#             nx = currx+dx[i]
#             ny = curry+dy[i]
#             if 0<= nx < n and 0<= ny <m:
#                 if arr[nx][ny] == 1:
#                     q.append((nx, ny))
#
#
# t = int(input())
# for tc in range(1, t+1):
#     m, n, v = map(int, input().split())
#     arr = [[0]*m for _ in range(n)]
#     tmp = []
#     for i in range(v):
#         e, s = map(int, input().split())
#         tmp.append((s, e))
#         arr[s][e] = 1
#     cnt = 0
#     for i, j in tmp:
#         if arr[i][j] == 1:
#             DFS(i, j)
#             cnt += 1
#     print(cnt)

def DFS(x, y):
    arr[x][y] = 0
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<n and 0<=ny<m:
            if arr[nx][ny]:
                DFS(nx, ny)


t = int(input())
for tc in range(1, t+1):
    m, n, v = map(int, input().split())
    arr = [[0]*m for _ in range(n)]
    for _ in range(v):
        x, y = map(int, input().split())
        arr[y][x] = 1
    cnt = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j]:
                DFS(i, j)
                cnt += 1
    print(cnt)
