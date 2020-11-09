import sys
sys.stdin = open('input.txt', 'r')

def check():
    for i in range(1, n):
        for j in range(1, n):
            arr[i][j] = min(arr[i-1][j], arr[i][j-1]) + arr[i][j]

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input())) for _ in range(n)]
    for i in range(1, n):
        arr[0][i] = arr[0][i-1] + arr[0][i]
    for i in range(1, n):
        arr[i][0] = arr[i-1][0] + arr[i][0]
    check()
    print('#{} {}'.format(tc, arr[n-1][n-1]))
