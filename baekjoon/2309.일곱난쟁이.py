arr = []
for _ in range(9):
    arr.append(int(input()))

sel = [0]*9
tmp = []
def powerset(idx):
    if idx == 9:
        if sel.count(1) == 7:
            li = []
            for i in range(9):
                if sel[i]:
                    li.append(arr[i])
            tmp.append(li)
        return
    powerset(idx+1)
    sel[idx] = 1
    powerset(idx+1)
    sel[idx] = 0

powerset(0)

for t in tmp:
    if sum(t) == 100:
        t.sort()
        for a in t:
            print(a)
        break