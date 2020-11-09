import sys
sys.stdin = open('input.txt', 'r')

import itertools

def check(nPr):
    global minV

    for i in range(len(nPr)):
        total = arr[0][nPr[i][0]]

        for j in range(0, len(nPr[i]) - 1):
            if minV <= total:
                break
            total += arr[nPr[i][j]][nPr[i][j + 1]]

        total += arr[nPr[i][-1]][0]
        if minV > total:
            minV = total

T = int(input())
for tc in range(1, T +1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    room = [n for n in range(1, N)]
    nPr = list(itertools.permutations(room, N - 1))
    minV = 10000
    check(nPr)
    print('#{} {}'.format(tc, minV))