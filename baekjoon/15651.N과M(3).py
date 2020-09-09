import sys
sys.stdin = open('input.txt', 'r')

n, m = map(int, input().split())

arr = [a for a in range(1, n+1)]
sel = [0]*m
visited = [0]*n

def perm(idx):
    if idx == m:
        for s in sel:
            print(s, end=' ')
        print()
        return

    for i in range(n):
        sel[idx] = arr[i]
        visited[i] = 1
        perm(idx+1)
        visited[i] = 0

perm(0)