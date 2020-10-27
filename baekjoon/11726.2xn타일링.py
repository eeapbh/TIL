n = int(input())
arr = [1, 2]
for i in range(n):
    if i >= 2:
        arr.append(arr[i-2] + arr[i-1])
print(arr[n-1]%10007)


