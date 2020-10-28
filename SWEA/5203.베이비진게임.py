import sys
sys.stdin = open('input.txt', 'r')

def perm(idx, arr):
    if idx == n:
        tmp = sel[:]
        perms.append(tmp)
        print(sel)
        return
    for i in range(n):
        if not visited[i]:
            sel[idx] = arr[i]
            visited[i] = 1
            perm(idx+1, arr)
            visited[i] = 0

t = int(input())
for tc in range(1, t+1):
    arr = list(map(int, input().split()))
    a = []
    b = []

    for i in range(3):
        a.append(arr[2*i])
        b.append(arr[2*i+1])
    n = len(a)
    sel = [0] * n
    visited = [0] * n
    perms = []
    perm(0, a)
    pa = perms[:]
    print(pa)
    perms = []
    perm(0, b)
    pb = perms[:]

    print('---')
    print(pb)
    ra = 0
    rb = 0
    for a in pa:
        if a[0] == a[1] and a[1] == a[2]:
            ra = 1
            break
        a = a.sort()
        if a[0] + 1 == a[1] and a[1] + 1 == a[2]:
            ra = 1
            break
    for b in pb:
        if b[0] == b[1] and b[1] == b[2]:
            rb = 1
            break
        b = b.sort()
        if b[0] + 1 == a[1] and b[1] + 1 == b[2]:
            rb = 1
            break
    if ra == 1 and rb == 1:
        print('#{} {}'.format(tc, 0))
        continue
    if ra == 1 and rb == 0:
        print('#{} {}'.format(tc, 1))
        continue
    if ra == 0 and rb == 1:
        print('#{} {}'.format(tc, 2))
        continue
    for j in range(3, 6):
        a.append(arr[j])
        b.append(arr[j+1])
        n = len(a)
        sel = [0] * n
        visited = [0] * n
        perms = []
        perm(0, a)
        perm(0, b)
        pa = perms[:]
        pb = perms[:]