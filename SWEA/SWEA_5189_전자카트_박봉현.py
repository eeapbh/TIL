import sys
sys.stdin = open('input.txt', 'r')

def check(row, total, cnt):
    if total > min(save):#백트레킹
        return
    if cnt == n and row == 0:
        save.append(total)
        return
    for i in range(n):
        if arr[row][i] and i not in cols:
            cols.append(i)

            check(i, total + arr[row][i], cnt + 1)
            cols.remove(i)

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    save = [100*n]
    cols = []
    total = 0
    cnt = 0
    check(0, total, 0)
    print('#{} {}'.format(tc, min(save)))
