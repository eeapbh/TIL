import sys
sys.stdin = open('input.txt', 'r')


def perm(idx, check):
    global ans
    if idx == n:
        total = abs(start[0]-sel[0][0]) + abs(start[1] - sel[0][1]) + abs(end[0]-sel[n-1][0]) + abs(end[1] - sel[n-1][1])
        for i in range(n - 1):
            total += abs(sel[i + 1][0] - sel[i][0]) + abs(sel[i + 1][1] - sel[i][1])
            if ans < total:
                break
        if ans > total:
            ans = total
        return
    for i in range(n):
        if check & (1<<i):
            continue
        sel[idx] = arr[i]
        perm(idx+1, check | (1<<i))


t = int(input())
for tc in range(1, t+1):
    n = int(input()) # 고객수
    info =list(map(int, input().split()))
    arr = []
    for i in range(2, n+2):
        a = info[2*i]
        b = info[2*i +1]
        arr.append((a, b))
    sel = [0]*n
    ans = 200*n
    start = (info[0], info[1])
    end = (info[2], info[3])
    perm(0, 0)
    print('#{} {}'.format(tc, ans))