import sys
sys.stdin = open('input.txt', 'r')

t = int(input())
keys = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
dic = {}
for tc in range(t):
    put1 = []
    put1 = input().split()
    num = put1[0]

    lists = input().split()
    for key in keys:
        count = 0
        for li in lists:
            if key == li:
                count +=1
        dic[key] = count
    print(num)
    for k, v in dic.items():
        for i in range(v):
            print(f'{k}', end=' ')


