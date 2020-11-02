import sys
from itertools import permutations
sys.stdin = open('input.txt', 'r')


t = int(input())
for tc in range(1, t+1):
    number, n = input().split()
    n = int(n)
    arr = []
    for i in number:
        arr.append(i)
    save = list(permutations(arr, len(number)))
    save.sort(reverse=True)
    rs = []
    for s in save:
        cnt = 0
        for i in range(len(number)):
            if s[i] != number[i]:
                cnt += 1
        if cnt == (2*n):
            rs.append(s)
    if len(rs) == 0:
        rs.append(arr)
    rs.sort(reverse=True)

    print('#{} {}'.format(tc, ''.join(rs[0])))
