import sys
sys.stdin = open('input.txt', 'r')


n, m = map(int, input().split())
arr = [a for a in range(1, n+1)]
sel = [0]*m
visited = [0]*n

def check(idx):

    if idx == m:
        for s in sel:
            print(s, end=' ')
        print()
        return
    for i in range(n):
        sel[idx] = arr[i]
        if idx > 0:
            if sel[idx] < sel[idx - 1]:
                continue
        visited[i] = 1
        check(idx+1)
        visited[i] = 0
check(0)