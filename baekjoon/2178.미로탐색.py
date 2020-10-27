import sys
sys.stdin = open('input.txt', 'r')

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 왜시간초과뜨지
# def BFS(x, y, c):
#     q = []
#     q.append((x, y, c))
#     while q:
#
#         currx, curry, currc = q.pop(0)
#         visit.append((currx, curry))
#         if currx == n-1 and curry == m-1:
#             return currc
#
#         for i in range(4):
#             nx = currx+dx[i]
#             ny = curry+dy[i]
#             if 0<=nx<n and 0<=ny<m and arr[nx][ny] == 1 and (nx, ny) not in visit:
#                 q.append((nx, ny, currc+1))
#
# n, m = map(int, input().split())
# arr = [list(map(int, input())) for _ in range(n)]
# visit = []
# cnt = 1
# tmp = []
# print(BFS(0, 0, cnt))
n, m = map(int, input().split())
arr = [list(map(int, input())) for _ in range(n)]
dist = [[0]*m for _ in range(n)]
q = []
check = [[0]*m for _ in range(n)]
q.append((0, 0))
check[0][0] = 1
dist[0][0] = 1
while q:
    x, y = q.pop(0)
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<n and 0<=ny<m:
            if check[nx][ny] == 0 and arr[nx][ny] == 1:
                q.append((nx, ny))
                dist[nx][ny] = dist[x][y] + 1
                check[nx][ny] = 1
print(dist[n-1][m-1])