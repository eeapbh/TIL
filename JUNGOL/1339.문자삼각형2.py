n = int(input())
m = n//2
k = -1
num = 0
arr = [[0]*n for _ in range(n)]
if 1<= n <= 100 and n%2 == 1:
    for i in range(m, -1, -1):
        k += 1
        for j in range(m-k, m+k+1, 1):
            num += 1
            if num == 27:
                num = 1
            arr[j][i] = num

    for i in range(n):
        for j in range(n):
            if arr[i][j] == 0:
                print(' ', end=' ')
            else:
                print(chr(64+arr[i][j]), end=' ')
        print()
else:
    print('INPUT ERROR')