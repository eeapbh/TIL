n, k = map(int, input().split())
arr = [[0, 0] for _ in range(7)]
for i in range(n):
    s, g = map(int, input().split())
    arr[g][s] += 1
cnt = 0

for i in range(1,7):
    for j in range(2):
        if arr[i][j] % k == 0:
            cnt += arr[i][j]//k
        else:
            cnt += arr[i][j]//k+1

print(cnt)


