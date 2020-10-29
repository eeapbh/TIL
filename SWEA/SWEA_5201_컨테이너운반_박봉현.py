import sys
sys.stdin = open('input.txt', 'r')

t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())

    weight = list(map(int, input().split()))
    jim = list(map(int, input().split()))
    weight = list(sorted(weight, reverse=True))
    jim = list(sorted(jim, reverse=True))

    total = 0
    for i in range(n):
        for j in range(m):
            if weight[i] <= jim[j]:
                total += weight[i]
                weight[i] = 150
                jim[j] = 0
                break
    print('#{} {}'.format(tc, total))