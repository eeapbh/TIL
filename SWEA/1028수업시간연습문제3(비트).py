cnt = 0
arr = [-1, 3, -9, 6, 7, -6, 1, 5, 4, -2]

n = len(arr)
for i in range(1<<n):

    tmp = []
    for j in range(n):
        if i & (1<<j):
            tmp.append(arr[j])
    if sum(tmp) == 0:
        print(tmp)
        cnt += 1
print(cnt)
