import sys
sys.stdin = open('input.txt', 'r')
t = int(input())
for tc in range(1, t+1):
    n, m, l = map(int, input().split())
    arr = [0]*(n+1)

    for i in range(m):
        a, b = map(int, input().split())
        arr[a] = b


    tmp = [[] for _ in range(n)]
    for i in range(n, 0, -1):
        arr[i//2] += arr[i]

    print('#{} {}'.format(tc, arr[l]))
