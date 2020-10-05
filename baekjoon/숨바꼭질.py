n, k = map(int, input().split())

cnt = 0
while 1:
    if k//2 > n:
        n = 2*n
        cnt += 1
    elif abs(k//2 - n) == 1:
        cnt += 2
        break
    else:
        if 2*n >k:
            n -= 1
            cnt += 1
    if n == k:
        break
print(cnt)
