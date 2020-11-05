import sys
sys.stdin = open('input.txt', 'r')

def dfs(x, cnt):
    if cnt == 3:
        return
    for i in range(1, n+1):
        if arr[x][i]:
            visit[i] += 1
            dfs(i, cnt+1)

t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    arr = [[0]*(n+1) for _ in range(n+1)]
    visit = [0]*(n+1)
    for i in range(m):
        a, b = map(int, input().split())
        arr[a][b] = 1
        arr[b][a] = 1

    dfs(1, 1)
    ans = 0
    for i in range(2, n+1):
        if visit[i]:
            ans += 1

    print('#{} {}'.format(tc, ans))