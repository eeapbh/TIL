n, m = map(int, input().split())
arr = [[0]*n for _ in range(n)]
arr[0][0] = 1
arr[1][0] = 1
arr[1][1] = 1
for i in range(n):
    for j in range(n):
        if j == 0 or j == i:
            arr[i][j] = 1

for i in range(n):
    for j in range(n):
        if i > 1:
            arr[i][j] = arr[i-1][j-1] + arr[i-1][j]
if m == 1:
    for i in range(n):
        for j in range(n):
            if arr[i][j]:
                print(arr[i][j], end=' ')
        print()
elif m == 2:
    for i in range(n-1, -1, -1):
        print(' ' *(n -i -1), end='')
        for j in range(n):
            if arr[i][j]:
                print(arr[i][j], end=' ')
        print()
elif m == 3:
    arr2 = list(zip(*arr))
    arr3 = []
    for i in arr2:
        arr3.append(i[::-1])

    for i in range(n-1, -1, -1):
        for j in range(n):
            if arr3[i][j]:
                print(arr3[i][j], end=' ')
        print()

