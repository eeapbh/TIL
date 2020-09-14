import sys
sys.stdin = open('input.txt', 'r')

import heapq

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = list(map(int, input().split()))
    heapq.heapify(arr)
    tmp = [0]
    tmp.extend(arr)
    result = 0
    while n >=1:
        n = n//2
        result += tmp[n]
    print('#{} {}'.format(tc, result))