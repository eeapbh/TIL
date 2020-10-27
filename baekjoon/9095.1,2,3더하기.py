t = int(input())

for i in range(t):
    arr = [1, 2, 4]
    n = int(input())
    for i in range(n):

        if i >= 3:
            arr.append(arr[i-3] + arr[i-2] + arr[i-1])
    print(arr[n-1])
