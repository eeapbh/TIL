n = int(input())
arr = []
for i in range(n):
    a = input().split()

    arr.append([int(a[0]), a[1]])

arr.sort(key=lambda x: (x[0]))
for i in arr:
    print(i[0], i[1])

