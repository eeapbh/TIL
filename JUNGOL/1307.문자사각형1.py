n = int(input())
arr = [[0]*n for _ in range(n)]
num = 0
for i in range(n-1, -1, -1):
    for j in range(n-1, -1, -1):
        num += 1
        if num == 27:
            num =1
        arr[j][i] = num

for i in range(n):
    for j in range(n):
        print(chr(64+arr[i][j]), end=' ')
    print()


