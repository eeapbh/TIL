n = int(input())
arr = [[] for _ in range(n+1)]
arr[0] = [1 for _ in range(10)]

for i in range(1, n+1):
    for j in range(10):
        arr[i].append(sum(arr[i-1][:j+1]))
print(arr[n][-1]%10007)