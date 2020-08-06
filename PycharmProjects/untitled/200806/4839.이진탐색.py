import sys
sys.stdin = open('input.txt', 'r')

t = int(input())
for tc in range(1, t+1):
    p, pa, pb = map(int, input().split())
    countA, countB =0, 0
    result = 0
    L = 1
    R = p
    while 1:

        c = int((L+R)/2)
        countA += 1
        if pa >c:
            L = c
        elif pa < c:
            R = c
        else:

            break
    L = 1
    R = p
    while 1:
        c = int((L + R) / 2)
        countB += 1
        if pb > c:
            L = c
        elif pb < c:
            R = c
        else:

            break
    if countA < countB:
        result = 'A'
    elif countA > countB:
        result = 'B'
    else:
        result = 0
    print(f'#{tc} {result}')