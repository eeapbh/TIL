t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    result = []
    total = 0
    for i in range(n-m+1):
        for j in range(n-m+1):
            for a in range(m):
                for b in range(m):
                    total += arr[i+a][j+b]

            result.append(total)
            total = 0
    print('#{} {}'.format(tc, max(result)))