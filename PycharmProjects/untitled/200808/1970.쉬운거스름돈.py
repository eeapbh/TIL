import sys
sys.stdin = open('input.txt', 'r')
t = int(input())

for tc in range(1, t+1):
    money = int(input())
    print(f'#{tc} ')
    if money >= 50000:
        mok = 0
        mok = money//50000
        money = money - 50000*mok
        print(mok, end = ' ')
    else:
        print(0, end = ' ')

    if money >= 10000:
        mok = 0
        mok = money//10000
        money = money - 10000*mok
        print(mok, end=' ')
    else:
        print(0, end = ' ')

    if money >= 5000:
        mok = 0
        mok = money // 5000
        money = money - 5000 * mok
        print(mok, end=' ')
    else:
        print(0, end=' ')

    if money >= 1000:
        mok = 0
        mok = money // 1000
        money = money - 1000 * mok
        print(mok, end=' ')
    else:
        print(0, end=' ')

    if money >= 500:
        mok = 0
        mok = money // 500
        money = money - 500 * mok
        print(mok, end=' ')
    else:
        print(0, end=' ')

    if money >= 100:
        mok = 0
        mok = money // 100
        money = money - 100 * mok
        print(mok, end=' ')
    else:
        print(0, end=' ')

    if money >= 50:
        mok = 0
        mok = money // 50
        money = money - 50 * mok
        print(mok, end=' ')
    else:
        print(0, end=' ')

    if money >= 10:
        mok = 0
        mok = money // 10
        money = money - 10 * mok
        print(mok, end=' ')
    else:
        print(0, end=' ')
    print()