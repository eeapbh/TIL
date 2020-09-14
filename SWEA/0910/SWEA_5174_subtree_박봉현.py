import sys
sys.stdin = open('input.txt', 'r')

def check(num):
    global cnt
    if arr[num][0]:
        cnt += 1
        check(arr[num][0])
    if arr[num][1]:
        cnt += 1
        check(arr[num][1])



t = int(input())
for tc in range(1, t+1):
    e, n = map(int, input().split())
    data = list(map(int, input().split()))

    arr = [[0]*2 for _ in range(e+2)]
    for i in range(e):
        p, c = data[2*i], data[(2*i)+1]
        if not arr[p][0]:
            arr[p][0] = c
        else:
            arr[p][1] = c
    cnt = 1
    check(n)

    print('#{} {}'.format(tc, cnt))
