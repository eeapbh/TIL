t = int(input())
for tc in range(1, t+1):
    a = input()
    numbers = list(input().split())
    keys = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
    print('#{}'.format(tc))
    for k in keys:
        cnt = numbers.count(k)
        for _ in range(cnt):
            print(k, end=' ')
