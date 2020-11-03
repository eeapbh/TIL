import sys
sys.stdin = open('input.txt', 'r')

def check(idx, cnt, rs):

    if cnt == n-1:
        if rs > max(save):
            save.append(rs)
        return
    visit[idx] = 0
    for i in range(n):
        if visit[i]:
            if rs*arr[cnt+1][i] > max(save):
                check(i, cnt+1, rs*arr[cnt+1][i])
                visit[i] = 1

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = [[int(x)/100 for x in input().split()] for _ in range(n)]
    save = [0]
    for i in range(n):
        visit = [1] * n
        check(i, 0, arr[0][i])
    ans = max(save)*100
    print('#{} {:6f}'.format(tc, ans))

