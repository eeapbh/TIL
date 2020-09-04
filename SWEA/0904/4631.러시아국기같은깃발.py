t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    arr = [list(input()) for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(m):
            if i == 0:
                if arr[i][j] != 'W':
                    cnt += 1
            elif 0<i<n:

            elif i == n:
                if arr[i][j] != 'R':
                    cnt += 1

