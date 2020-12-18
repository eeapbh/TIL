n, m = map(int, input().split())
mid = (n//2)+1
if n % 2 == 0 or n > 100 or m < 1 or m > 4:
    print('INPUT ERROR!')
elif m == 1:
    for i in range(1, mid + 1):
        print('*' * i)
    for i in range(mid - 1, 0, -1):
        print('*' * i)
elif m == 2:
    for i in range(1, mid + 1):
        print(' ' * (mid -i), end='')
        print('*' * i)
    for i in range(1, mid):
        print(' ' * i, end='')
        print('*' * (mid -i))

elif m == 3:
    for i in range(mid, 0, -1):
        print(' ' * (mid-i), end='')
        print('*' * ((2 * i) - 1))
    for i in range(1, mid):
        print(' ' * (mid-i-1), end='')
        print('*' * ((2 * i) + 1))
elif m == 4:
    for i in range(mid, 0, -1):
        print(' ' * (mid-i), end='')
        print('*' * i)
    for i in range(2, mid+1):
        print(' ' * (mid-1), end='')
        print('*' * i)




