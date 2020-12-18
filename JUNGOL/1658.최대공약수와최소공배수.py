n, m = map(int, input().split())
arr1 = []
arr2 = []
for i in range(1, n+1):
    if n % i == 0:
        arr1.append(i)

for i in range(1, m+1):
    if m % i == 0:
        arr2.append(i)

# print(arr1, arr2)
for i in range(len(arr1)-1, -1, -1):
    if arr1[i] in arr2:
        ans1 = arr1[i]
        break


ans2 = n // ans1 * m
print(ans1)
print(ans2)

