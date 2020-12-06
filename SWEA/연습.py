import sys
sys.stdin = open('input.txt', 'r')

def check(x, y):
    global first, second
    tmp = arr[x][y:y+m]
    max_cost = 0
    for i in range(1<<m):
        sum_honey = sum_cost = 0
        for j in range(m):
            if i & (1<<j):
                sum_honey += tmp[j]
                sum_cost += tmp[j]**2
        if sum_honey <= c:
            max_cost = max(max_cost, sum_cost)

    if max_cost > first[0]:
        if x == first[1] and y < first[2] + m:
            first = [max_cost, x, y]
        else:
            second = first[:]
            first = [max_cost, x, y]
    elif max_cost > second[0]:
        if x != first[1] or y >= first[2] + m:
            second = [max_cost, x, y]


t = int(input())
for tc in range(1, t+1):
    n, m, c = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    first = [0, 0, 0]
    second = [0, 0, 0]
    for i in range(n):
        for j in range(n-m+1):
            check(i, j)

    print('#{} {}'.format(tc, first[0]+second[0]))