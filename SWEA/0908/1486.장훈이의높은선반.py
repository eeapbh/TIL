def powerset(idx):
    if idx == n:
        hab = 0
        for i in range(n):
            if sel[i]:
                hab += arr[i]
        total.append(hab)
        return
    sel[idx] = 1
    powerset(idx+1)
    sel[idx] = 0
    powerset(idx+1)


t = int(input())
for tc in range(1, t+1):
    n, b = map(int, input().split())
    arr = list(map(int, input().split()))
    total = []
    sel = [0]*n
    powerset(0)
    result = []
    for i in total:
        if i >= b:
            result.append(i-b)
    print('#{} {}'.format(tc, min(result)))


