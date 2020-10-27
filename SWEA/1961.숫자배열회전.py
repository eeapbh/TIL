import sys
sys.stdin = open('input.txt', 'r')

t = int(input())
def spin(arr):
    arr2 = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            arr2[i][j] = arr[n-1-j][i]
    return arr2

for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    arr90 = spin(arr)
    arr180 = spin(arr90)
    arr270 = spin(arr180)
    print('#{}'.format(tc))
    for i in range(n):
        for j in range(n):
            print(arr90[i][j], end='')
        print(end=' ')
        for j in range(n):
            print(arr180[i][j], end='')
        print(end=' ')
        for j in range(n):
            print(arr270[i][j], end='')
        print()