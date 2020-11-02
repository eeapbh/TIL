import sys
sys.stdin = open('input.txt', 'r')


def check(idx, total):
    global max_value
    if total <= max_value:
        return
    if idx>= n:
        max_value = total
        return
    for i in range(n):
        if visit[i]:
            visit[i] = 0
            check(idx+1, total*(arr[idx][i]))
            visit[i] = 1

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visit = [1] * n
    max_value = 0
    check(0, 100)
    print('#{} {:6f}'.format(tc, max_value/(100**n)))