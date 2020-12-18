n, m = map(int, input().split())
if m < 0 or m > 3 or n > 100 or n <= 0:
    print("INPUT ERROR!")
elif m == 1:
    for i in range(1, n+1):
        print('*'*i)

elif m == 2:
    for i in range(n, 0, -1):
        print('*'*i)

elif m == 3:
    for i in range(1, n+1):
        print(' '* (n -i), end='')
        print('*' * ((2 * i) - 1) )

