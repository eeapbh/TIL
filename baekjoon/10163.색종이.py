import sys
sys.stdin = open('input.txt', 'r')

arr = [[0]*101 for _ in range(101)]
N = int(input())
num = 1
for i in range(N):
    x, y, m, n = map(int, input().split())
    for a in range(x, x+m):
        for b in range(y, y+n):
            arr[a][b] = num
    num += 1


for i in range(1, N+1):
    cnt = 0
    for r in range(101):
        cnt += arr[r].count(i)
    print(cnt)