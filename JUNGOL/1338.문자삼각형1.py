n = int(input())
arr = [[0]*n for _ in range(n)]
sx = 0
cnt = 0
num = 1
while 1:
    sy = n-1
    for i in range(sx, n):
        arr[i][sy] = num
        num += 1
        if num == 27:
            num = 1
        sy -= 1
    sx += 1
    if sx == n:
        break

for i in range(n):
    for j in range(n):
        if arr[i][j] == 0:
            print(' ', end=' ')
        else:
            print(chr(64 + arr[i][j]), end=' ')
    print()