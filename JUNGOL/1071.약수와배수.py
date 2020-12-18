n = int(input())
arr = list(map(int, input().split()))
m = int(input())
ans1 = ans2 = 0

for i in range(n):
    if m % arr[i] == 0:
        ans1 += arr[i]
    if arr[i] % m == 0:
        ans2 += arr[i]

print(ans1)
print(ans2)