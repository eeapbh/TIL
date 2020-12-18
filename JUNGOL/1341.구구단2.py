s, e = map(int, input().split())
if s - e <= 0:
    for i in range(s, e + 1):
        cnt = 0
        for j in range(1, 10):
            if i * j < 10:
                print('{} * {} =  {}'.format(i, j, i * j), end='   ')
            else:
                print('{} * {} = {}'.format(i, j, i * j), end='   ')
            cnt += 1
            if (cnt % 3) == 0 and cnt != 0:
                print()
        print()

else:
    for i in range(s, e - 1, -1):
        cnt = 0
        for j in range(1, 10):
            if i * j < 10:
                print('{} * {} =  {}'.format(i, j, i * j), end='   ')
            else:
                print('{} * {} = {}'.format(i, j, i * j), end='   ')
            cnt += 1
            if (cnt % 3) == 0 and cnt != 0:
                print()
        print()



