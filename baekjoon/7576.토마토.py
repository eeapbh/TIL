import sys
from collections import deque
sys.stdin = open('input.txt', 'r')

# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
#
#
# m, n = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(n)]
# c = 0 # 처음에 -1의 갯수
#
# for i in arr:
#     c += i.count(-1)
#
# cnt = (m*n) - c # 토마토의 갯수
#
# def check():
#     day = 0
#     while 1:
#         c2 = 0  #1얼마나 있는지 찾기위함
#         save = []
#         for i in range(n):
#             for j in range(m):
#                 if arr[i][j] == 1:
#                     save.append((i, j))
#         for s in save:
#             x = s[0]
#             y = s[1]
#             for i in range(4):
#                 nx = x+dx[i]
#                 ny = y+dy[i]
#                 if 0<=nx<n and 0<=ny<m and arr[nx][ny] ==0:
#                     arr[nx][ny] = 1
#
#         for i in arr:
#             c2 += i.count(1)
#
#         day += 1
#         if c2 == cnt: #토마토가 빈곳빼고 다들어가있으면
#             if day == 1:
#                 return day-1
#             return day
#
#         if day > m*n:
#             day = -1
#             return day
# print(check())

def bfs(q, ans):
    cnt = ans
    while q:
        v = q.popleft()
        cx = v[0]
        cy = v[1]
        cnt = v[2]
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0<=nx<n and 0<=ny<m:
                if arr[nx][ny] == 0 and arr[nx][ny] != -1:
                    arr[nx][ny] = 1
                    q.append([nx, ny, cnt+1])
    return cnt


def check(ans, arr):
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                return -1
    return ans

m, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
ans = 0
q = deque([])
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            q.append([i, j, ans])
ans = bfs(q, ans)
print(check(ans, arr))
