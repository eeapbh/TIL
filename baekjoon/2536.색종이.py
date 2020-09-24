import sys
sys.stdin = open('input.txt', 'r')

n = int(input())
arr = [[0]*100 for _ in range(100)]
for _ in range(n):
    x, y = map(int, input().split())
    for i in range(y-1, y+9):
        for j in range(x-1, x+9):
            arr[i][j] = 1
cnt = 0
for i in range(100):
    for j in range(100):
        if arr[i][j] == 1:
            cnt += 1

print(cnt)