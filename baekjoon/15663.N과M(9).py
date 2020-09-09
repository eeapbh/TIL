import sys
sys.stdin = open('input.txt', 'r')
def perm(idx):
    if idx == m:
        print(sel)
        if sel not in total:
            total.append(sel)
        return

    for i in range(n):
        if not visited[i]:
            sel[idx] = arr[i]
            visited[i] = 1
            perm(idx+1)
            visited[i] = 0

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
sel = [0]*m
visited = [0]*n
total = []


perm(0)
print(total)