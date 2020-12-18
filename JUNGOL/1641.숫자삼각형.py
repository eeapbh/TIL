n, m = map(int, input().split())
arr = [[0]*n for _ in range(n)]
if n % 2 == 0 or n > 100 or m < 1 or m > 3:
    print('INPUT ERROR!')
elif m == 1:
    cnt = 0
    num = 0
    for i in range(n):
        if i % 2 == 0:
            cnt += 1
            for j in range(cnt):
                num += 1
                arr[i][j] = num
        else:
            cnt += 1
            for j in range(cnt-1, -1, -1):
                num += 1
                arr[i][j] = num

    for i in range(n):
        for j in range(n):
            if arr[i][j]:
                print(arr[i][j], end=' ')
        print()
elif m == 2:
    num = -1
    for i in range(n):
        print(' ' * (i * 2), end='')
        for j in range((2*(n-i)) -1):

            print(i, end=' ')
        print()
elif m == 3:
    mid = n//2 + 1
    for i in range(1, mid+1):
        for j in range(1, i+1):
            print(j, end=' ')
        print()
    for i in range(mid-1, 0, -1):
        for j in range(1, i+1):
            print(j, end=' ')
        print()
