import sys
sys.stdin = open('input.txt', 'r')

from itertools import permutations
t = int(input())
for tc in range(1, t+1):
    n = int(input()) # 고객수
    info =list(map(int, input().split()))
    arr = []
    for i in range(2, n+2):
        a = info[2*i]
        b = info[2*i +1]
        arr.append((a, b))
    start = (info[0], info[1])
    end = (info[2], info[3])
    # print(start, end)
    # print(arr)
    perm = list(permutations(arr))
    ans = 200*n
    for p in perm:
        total = abs(start[0]-p[0][0]) + abs(start[1] - p[0][1]) + abs(end[0]-p[n-1][0]) + abs(end[1] - p[n-1][1])
        if ans < total:
            break
        for i in range(n-1):
            total += abs(p[i+1][0] - p[i][0]) + abs(p[i+1][1] - p[i][1])
            if ans < total:
                break
        if ans > total:
            ans = total
    print('#{} {}'.format(tc, ans))