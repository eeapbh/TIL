import sys
sys.stdin = open('input.txt', 'r')
n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
sel = [0]*m
visited = [0]*n
def perm(idx):
    if idx == m:
        for s in sel:
            print(s, end=' ')
        print()
        return
    for i in range(n):
        if not visited[i]:
            sel[idx] = arr[i]
            visited[i] = 1
            perm(idx+1)
            visited[i] = 0
perm(0)