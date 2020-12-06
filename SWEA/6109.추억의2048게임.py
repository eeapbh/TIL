import sys
sys.stdin = open('input.txt', 'r')

t = int(input())
for tc in range(1, t+1):
    n, s = input().split()
    n = int(n)
    arr = [list(map(int, input().split())) for _ in range(n)]
    if s == 'up':
        for i in range(n):
            for j in range(n):
                if j > 0:
                    if arr[j][i]:
                        if arr[j-1][i] == 0:
                            arr[j][i], arr[j-1][i] = arr[j-1][i], arr[j][i]
                        else:
                            if arr[j][i] == arr[j-1][i]:
                                arr[j][i] = 0
                                arr[j-1][i] = 2*arr[j][i]
    for a in arr:
        print(a)
