import copy
n = 6
arr = [[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18], [19, 20, 21, 22, 23, 24], [25, 26, 27, 28, 29, 30], [31, 32, 33, 34, 35, 36]]
def spin90(arr):
    Narr = [[0]*m for _ in range(m)]
    for i in range(m):
        for j in range(m):
            Narr[i][j] = arr[n-j-1][i]
    return Narr

for i in range(n//2):
    m = n-2*i
    tmp = []
    for j in range(i, n-i):
        tmp.append(arr[j][i:n-i])
    print(f'{i}번째')
    print(tmp)
    if i & 2== 0:
        arr2 = spin90(tmp)
    else:
        arr2 = spin90(spin90(spin90(tmp)))


    for a in range(i, n-i):
        for b in range(len(arr2)):
            arr[a][i:n-i] = arr2[b]
    print(arr)

