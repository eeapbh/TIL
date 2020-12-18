
while 1:
    s, e = map(int, input().split())

    if s < 2 or s > 9 or e < 2 or e > 9:
        print('INPUT ERROR!')

    elif s-e >= 0:
        for j in range(1, 10):
            for i in range(s, e-1, -1):
                if i*j <10:
                    print('{} * {} =  {}'.format(i, j, i * j), end='   ')
                else:
                    print('{} * {} = {}'.format(i, j, i*j), end='   ')
            print()
    elif s-e < 0:
        for j in range(1, 10):
            for i in range(s, e+1):
                if i*j <10:
                    print('{} * {} =  {}'.format(i, j, i * j), end='   ')
                else:
                    print('{} * {} = {}'.format(i, j, i*j), end='   ')
            print()
