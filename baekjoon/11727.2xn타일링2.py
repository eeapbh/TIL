n = int(input())
arr = [1, 3, 5]
for i in range(n):
    if i >= 3:
        arr.append(arr[i-1] + (2*arr[i-2]))

print(arr[n-1] % 10007)