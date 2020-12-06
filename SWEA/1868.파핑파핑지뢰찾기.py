import sys
sys.stdin = open('input.txt', 'r')
from collections import deque
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

def BFS(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    while q:
        cx, cy = q.popleft()
        for i in range(8):
            nx = cx+dx[i]
            ny = cy+dy[i]
            if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:
                visited[nx][ny] = True
                if arr[nx][ny] == 0: # 연쇄적으로 클릭할수 있으면 클릭
                    q.append((nx, ny))


def mine_check(x, y):
    cnt = 0
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<n:
            if arr[nx][ny] == '*':
                cnt += 1
    return cnt

for tc in range(1, int(input())+1):
    n = int(input())
    arr = [list(input()) for _ in range(n)]
    # 내주변의 지뢰의 수로 2차원 리스트를 갱신
    zero_list = []
    for i in range(n):
        for j in range(n):
            if arr[i][j] == '.':
                arr[i][j] = mine_check(i, j)
            if arr[i][j] == 0:
                zero_list.append((i, j))
    ans = 0
    # 주변에 지뢰가 하나도 없는 값들은 먼저 클릭
    visited = [[False]*n for _ in range(n)]
    for x, y in zero_list:
        if visited[x][y]:
            continue
        BFS(x, y)
        ans += 1
    # 나머지 지뢰가 아닌 칸들을 클릭
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and arr[i][j] != '*':
                ans += 1
    print('#{} {}'.format(tc, ans))
# dx = [-1, -1, -1, 0, 1, 1, 1, 0]
# dy = [-1, 0, 1, 1, 1, 0, -1, -1]
#
# def bfs(x, y):
#     q = deque()
#     q.append((x, y))
#     visit[x][y] = 1
#     while q:
#         cx, cy = q.popleft()
#         for i in range(8):
#             nx = cx+dx[i]
#             ny = cy+dy[i]
#             if 0<=nx<n and 0<=ny<n and visit[nx][ny] == 0:
#                 visit[nx][ny] = 1
#                 if arr[nx][ny] == 0:
#                     q.append((nx, ny))
#                     # arr[nx][ny] = 1
# def check(x, y):
#     cnt = 0
#     for i in range(8):
#         nx = x+dx[i]
#         ny = y+dy[i]
#         if 0<=nx<n and 0<=ny<n:
#            if arr[nx][ny] == '*':
#                cnt += 1
#     return cnt
#
# t = int(input())
# for tc in range(1, t+1):
#     n = int(input())
#     arr = [list(input()) for _ in range(n)]
#     # zero = []
#     for i in range(n):
#         for j in range(n):
#             if arr[i][j] == '.':
#                 arr[i][j] = check(i, j)
#             # if arr[i][j] == 0:
#             #     zero.append((i, j))
#     ans = 0
#     visit = [[0]*n for _ in range(n)]
#     for i in range(n):
#         for j in range(n):
#             if arr[i][j] == 0 and visit[i][j] == 0:
#                 bfs(i, j)
#                 ans += 1
#
#     for i in range(n):
#         for j in range(n):
#             if not visit[i][j] and arr[i][j] != '*':
#                 ans += 1
#     print('#{} {}'.format(tc, ans))