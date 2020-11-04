import sys
sys.stdin = open('input.txt', 'r')

def check(flag, idx, total):
    global ans
    if flag == (1<<n)-1:
        if ans > total:
            ans = total
        return
    if total > ans:
        return
    for i in range(n):
        if flag & (1<<i):
            continue
        check(flag | 1<<i, idx +1, total+arr[idx][i])


t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    ans = 99*n
    check(0, 0, 0)
    print('#{} {}'.format(tc, ans))
