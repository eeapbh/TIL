t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = []
    for i in range(n):
        for j in range(n):
            arr[i][0] = 1
            arr[i][j] = 1

            arr[i][j] = arr[i-1][j-1]+arr[i-1][j]
    print(arr)