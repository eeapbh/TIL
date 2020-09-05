import sys
sys.stdin = open('input.txt', 'r')


t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    arr = [list(input()) for _ in range(n)]

    result = n*m
    cnt1 = 0
    for w in range(0, n-2):
        for j in range(0, m):
            if arr[w][j] != 'W':
                cnt1 += 1

        cnt2 = 0
        for b in range(w+1, n-1):
            for j in range(0, m):
                if arr[b][j] != 'B':
                    cnt2 += 1

            cnt3 = 0
            for r in range(b+1, n):
                for j in range(0, m):
                    if arr[r][j] != 'R':
                        cnt3 += 1

            cnt = cnt1 + cnt2 + cnt3
            if result > cnt:
                result = cnt
    print('#{} {}'.format(tc, result))

