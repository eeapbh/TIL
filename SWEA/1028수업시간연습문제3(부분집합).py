def powerset(idx):
    if idx == n:
        tmp = []
        for s in range(n):
            if sel[s]:
                tmp.append(arr[s])
        rs.append(tmp)
        return
    sel[idx] = 1
    powerset(idx + 1)
    sel[idx] = 0
    powerset(idx + 1)

arr = [-1, 3, -9, 6, 7, -6, 1, 5, 4, -2]
sel = [0]*10
n = 10
rs = []
powerset(0)
cnt = 0
for r in rs:
    if sum(r) == 0:
        print(r)
        cnt += 1
print(cnt)