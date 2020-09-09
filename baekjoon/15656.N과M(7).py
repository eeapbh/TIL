import sys
sys.stdin = open('input.txt', 'r')

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

sel = [0]*m

def perm(idx):
    if idx == m:
        for s in sel:
            print(s, end=' ')
        print()
        return
    for i in range(n):
        sel[idx] = arr[i]

        perm(idx+1)


perm(0)