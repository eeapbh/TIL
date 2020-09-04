import sys
sys.stdin = open('input.txt', 'r')

t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    pizza = list(map(int, input().split()))
    oven = []
    for i in range(n):
        oven.append([pizza[i], i])

    i = 0
    while len(oven) > 1:
        oven[0][0] = oven[0][0]// 2

        if oven[0][0] == 0:
            if n+i < m:
                oven.pop(0)
                oven.append([pizza[n+i], n+i])
                i+= 1
            elif n+i >= m:
                oven.pop(0)
        else:
            oven.append(oven.pop(0))

    print('#{} {}'.format(tc, oven[0][1]+1))