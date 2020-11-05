import sys
sys.stdin = open('input.txt', 'r')

def dfs(x):
    for i in range(n+1):
        if arr[x][i]:
            arr[x][i] = 0
            arr[i][x] = 0
            dfs(i)

t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    info = list(map(int, input().split()))
    arr = [[0]*(n+1) for _ in range(n+1)]
    visit = [0]*(n+1)
    for i in range(m):
        arr[info[2*i]][info[(2*i)+1]] = 1
        arr[info[(2*i)+1]][info[2*i]] = 1


    cnt = 0
    for a in arr:
        if sum(a) == 0:
            cnt +=1
    for i in range(n+1):
        for j in range(n+1):
            if arr[i][j] == 1:
                dfs(i)
                cnt += 1

    print('#{} {}'.format(tc, cnt-1))