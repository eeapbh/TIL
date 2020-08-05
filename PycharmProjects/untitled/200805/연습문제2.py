N = 10
k = 0
arr = list(map(int, input().split()))
cnt = 0
for i in range(1<<N):
    SUM = 0
    sub = []
    for j in range(N):
        if i & (1<<j):
            sub.append(arr[j])
            SUM += arr[j]

    if SUM == k:
        cnt +=1
        print(sub)
print(f'{})