import sys
sys.stdin = open('input.txt', 'r')

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    li = []
    for i in range(n):
        li.append(list(map(int, input().split())))
    li.sort(key=lambda x : x[1])
    result = 0
    finish = 0
    while li:
        start, end = li.pop(0)
        if start >= finish:
            result += 1
            finish = end
    print('#{} {}'.format(tc, result))


