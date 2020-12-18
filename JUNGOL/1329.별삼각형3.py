n = int(input())
m = (n//2) #3
if n % 2 == 0 or n > 100:
    print('INPUT ERROR!')
else:
    for i in range(m+1):
        print(' ' * i, end='')
        print('*' * ((2 * i) + 1))
    for i in range(m-1, -1, -1):
        print(' ' * i, end='')
        print('*' * ((2 * i) + 1))
