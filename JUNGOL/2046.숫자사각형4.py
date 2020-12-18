n, m = map(int, input().split())
arr = [[0]*n for _ in range(n)]

if m == 1:
    num = 0
    for i in range(n):
        num += 1
        for j in range(n):
            print(num, end=' ')
        print()
elif m == 2:
    for i in range(n):
        if i % 2 == 0:
            for j in range(1, n+1):
                print(j, end=' ')
        else:
            for j in range(n, 0, -1):
                print(j, end=' ')
        print()
elif m == 3:
    for i in range(1, n+1):
        for j in range(1, n+1):
            print(i*j, end=' ')
        print()


