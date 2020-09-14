import sys
sys.stdin = open('input.txt', 'r')

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
sel = [0]*m
visited = [0]*n
total = set()
def perm(idx):
    if idx == m:
        total.add(tuple(sel))
        return

    for i in range(n):
        sel[idx] = arr[i]
        if idx>0:
            if sel[idx] < sel[idx-1]:
                continue
        visited[i] = 1
        perm(idx+1)
        visited[i] = 0
perm(0)
b = sorted(total)
for t in b:
    print(*t)

