import sys
sys.stdin = open('input.txt', 'r')
n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

sel = [0]*n

def powerset(idx):
    if idx == n:
        if sel.count(1) == m:
            for i in range(n):
                if sel[i]:
                    print(arr[i], end=' ')
            print()
        return
    sel[idx] = 1
    powerset(idx+1)
    sel[idx] = 0
    powerset(idx+1)

powerset(0)