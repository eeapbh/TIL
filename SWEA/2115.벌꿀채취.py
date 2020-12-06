import sys
sys.stdin = open('input.txt','r')

def check(idx, sum_honey, sum_cost):
    global max_cost
    if sum_honey > c:
        return
    max_cost = max(max_cost, sum_cost)
    for i in range(idx, m):
        check(i+1, sum_honey+tmp[i], sum_cost + tmp[i]**2)

t = int(input())
for tc in range(1, t+1):
    n, m, c = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    save = []
    for i in range(n):
        for j in range(n-m+1):
            tmp = arr[i][j:j+m]
            max_cost = 0
            check(0, 0, 0)
            save.append([max_cost, i, j])
    save.sort(reverse=True)

    first = save.pop(0)
    for cost, i, j in save:
        if i == first[1] and first[2]-m < j < first[2]+m:
            continue
        second = [cost, i, j]
        break
    print('#{} {}'.format(tc, first[0] + second[0]))