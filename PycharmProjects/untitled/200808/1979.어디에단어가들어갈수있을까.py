import sys
sys.stdin = open('input.txt', 'r')
t = int(input())
for tc in range(1, t+1):
    n, k = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    long = 0
    result = []
    for i in range(n):
        long = 0
        for j in range(n):
            if arr[i][j]:
                long += 1
            else:
                result.append(long)
                long = 0
        result.append(long)
    for i in range(n):
        long = 0
        for j in range(n):
            if arr[j][i]:
                long += 1
            else:
                result.append(long)
                long = 0
        result.append(long)


    print(f'#{tc} {result.count(k)}')