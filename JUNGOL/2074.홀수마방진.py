n = int(input())
arr = [[0]*n for _ in range(n)]
num = 1
x = 0
y = n//2
arr[x][y] = 1
while 1:
    num += 1
    if num % n == 1 and num > 1:
        x = x + 1
    else:
        x = x - 1
        y = y - 1

    if x < 0:
        x = n - 1
    if y < 0:
        y = n - 1

    arr[x][y] = num
    if num == n*n:
        break

for i in range(n):
    for j in range(n):
        print(arr[i][j], end=' ')
    print()




