import sys
sys.stdin = open('input.txt', 'r')

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
sel = [0]*n
total = set()
def powerset(idx):
    if idx == n:
        if sel.count(1) == m:
            tmp = []
            for i in range(n):
                copyArr = arr[:]
                if sel[i]:
                    tmp.append(copyArr[i])
            total.add(tuple(tmp))
        return

    sel[idx] = 1
    powerset(idx+1)
    sel[idx] = 0
    powerset(idx+1)

powerset(0)
b = sorted(total)
for t in b:
    print(*t)


