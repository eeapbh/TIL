import sys
sys.stdin = open('input.txt', 'r')

t = int(input())
for tc in range(1, t+1):
    n, k = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    cnt = 0
    for i in range(n):
        tmp = []
        for j in range(n):
            if arr[i][j] == 1:
                tmp.append(arr[i][j])
            else:
                tmp = []

            if len(tmp) == k:
                if j+1<n:
                    if arr[i][j+1] == 0:
                        cnt += 1
                        tmp = []
                if j == n-1:
                    cnt += 1
                    tmp = []
    arr2 = list(zip(*arr))
    for i in range(n):
        tmp = []
        for j in range(n):
            if arr2[i][j] == 1:
                tmp.append(arr2[i][j])
            else:
                tmp = []

            if len(tmp) == k:
                if j+1<n:
                    if arr2[i][j+1] == 0:
                        cnt += 1
                        tmp = []
                if j == n-1:
                    cnt += 1
                    tmp = []
    print('#{} {}'.format(tc, cnt))


