import sys
sys.stdin = open('input.txt', 'r')

def go(idx):
    global cnt, d
    can = arr[idx]
    big = 0
    for i in range(idx+1, idx+can+1):
        if arr[i] > big:
            big = arr[i]
            next = i
    print(next, arr[next])
    d += arr[idx]
    d += big
    # next = idx + max(tmp)
    cnt += 1
    if d > n:
        return
    return go(next)

t = int(input())
for tc in range(1, t+1):
    info = list(map(int, input().split()))
    n = info[0]
    arr = info[1:]
    arr.append(0)
    print(arr)
    cnt = 0
    d = 0
    go(0)
    print('#{} {}'.format(tc, cnt))

