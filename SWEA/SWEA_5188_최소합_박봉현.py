import sys
sys.stdin = open('input.txt', 'r')

dx = [1, 0]
dy = [0, 1]

def dfs(x, y, total):
    if x == n-1 and y == n-1:
        save.append(total)


    for i in range(2):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<n:
            if total + arr[nx][ny] < min(save):#백트레킹
                dfs(nx, ny, total + arr[nx][ny])

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    save = [n*10]
    dfs(0, 0, arr[0][0])
    print('#{} {}'.format(tc, min(save)))

# dp로
# t = int(input())
# for tc in range(1, t+1):
#     n = int(input())
#     arr = [list(map(int, input().split())) for _ in range(n)]
#
#     for i in range(1, n):
#         arr[0][i] = arr[0][i-1] + arr[0][i]
#         arr[i][0] = arr[i-1][0] + arr[i][0]
#     for i in range(1, n):
#         for j in range(1, n):
#             arr[i][j] = min(arr[i-1][j], arr[i][j-1]) + arr[i][j]
#
#     print('#{} {}'.format(tc, arr[n-1][n-1]))