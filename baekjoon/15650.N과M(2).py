import sys
sys.stdin = open('input.txt', 'r')

n, m = map(int, input().split())

arr = [a for a in range(1, n+1)]
sel = [0]*n

def powerset(idx):
    if idx == n:
        if  sel.count(1) == m:
            for s in range(n):
                if sel[s]:
                    print(arr[s], end=' ')
            print()
        return

    sel[idx] = 1
    powerset(idx+1)
    sel[idx] = 0
    powerset(idx+1)

powerset(0)