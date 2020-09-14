import sys
sys.stdin = open('input.txt', 'r')

def DFS(x):
    visited[i] = 1
    for y in range(1, n+1):
        if arr[x][y] == 1 and visited[y] == 0:
            visited[y] = 1
            DFS(y)


t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    arr = [[0]*(n+1) for _ in range(n+1)]
    visited = [0]*(n+1)
    for i in range(m):
        a, b = map(int, input().split())
        arr[a][b] = arr[b][a] = 1

    cnt = 0
    for i in range(1, n+1):
        if not visited[i]:

            DFS(i)
            cnt += 1

    print('#{} {}'.format(tc, cnt))