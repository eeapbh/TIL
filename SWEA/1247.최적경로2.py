import sys
sys.stdin = open('input.txt', 'r')


def perm(idx):
    global ans
    if idx == n:
        total = abs(start[0]-arr[0][0]) + abs(start[1] - arr[0][1]) + abs(end[0]-arr[n-1][0]) + abs(end[1] - arr[n-1][1])
        for i in range(n - 1):
            total += abs(arr[i + 1][0] - arr[i][0]) + abs(arr[i + 1][1] - arr[i][1])
            if ans < total:
                break
        if ans > total:
            ans = total
        return
    for i in range(idx, n):
        arr[i], arr[idx] = arr[idx], arr[i]
        perm(idx+1)
        arr[i], arr[idx] = arr[idx], arr[i]

t = int(input())
for tc in range(1, t+1):
    n = int(input()) # 고객수
    info =list(map(int, input().split()))
    arr = []
    for i in range(2, n+2):
        a = info[2*i]
        b = info[2*i +1]
        arr.append((a, b))

    ans = 200*n
    start = (info[0], info[1])
    end = (info[2], info[3])
    perm(0)
    print('#{} {}'.format(tc, ans))